#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <EGL/egl.h>
#include <EGL/eglext.h>

#include <xcb/xcb.h>

int main(int argc, char const *argv[])
{

	// EGL base initialization

	EGLint majorVersion;
	EGLint minorVersion;
	EGLDisplay display;

	display = eglGetDisplay(EGL_DEFAULT_DISPLAY);

	if (display == EGL_NO_DISPLAY) {
		std::cout << "Can't get display." << std::endl;
		return 1;
	}

	if(!eglInitialize(display, &majorVersion, &minorVersion)) {
		std::cout << "Can't initialize display." << std::endl;
		return 1;
	}

	std::cout << "EGL version: " << majorVersion << "." << minorVersion << std::endl;

	EGLint numConfigs = 0;
	const EGLint maxConfigs = 10;
	EGLConfig configs[10];

	EGLint attribList[] = 
	{
		EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
		EGL_RED_SIZE, 8,
		EGL_GREEN_SIZE, 8,
		EGL_BLUE_SIZE, 8,
		EGL_DEPTH_SIZE, 1,
		EGL_NONE
	};

	if (!eglChooseConfig(display, attribList, configs, maxConfigs, &numConfigs)) {
		std::cout << "Can't get number of configs." << std::endl;
		return 1;	
	} else {
		std::cout << "Configs: " << numConfigs << std::endl;
	}

	// XCB stuff
	// Copied from http://rosettacode.org/wiki/Window_creation/X11
	xcb_connection_t *connection;
	xcb_screen_t *screen;
	xcb_drawable_t native_window;
	xcb_gcontext_t foreground;
	xcb_gcontext_t background;
	xcb_generic_event_t *e;

	uint32_t mask = 0;
	uint32_t values[2];

	connection = xcb_connect(NULL, NULL);

	screen = xcb_setup_roots_iterator(xcb_get_setup(connection)).data;
	native_window = screen->root; //temporarily assing to setup the contexts

	// black foreground context
	foreground = xcb_generate_id(connection);
	mask = XCB_GC_FOREGROUND | XCB_GC_GRAPHICS_EXPOSURES;
	values[0] = screen->black_pixel;
	values[1] = 0;
	xcb_create_gc(connection, foreground, native_window, mask, values);

	// white background context
	background = xcb_generate_id(connection);
	mask = XCB_GC_BACKGROUND | XCB_GC_GRAPHICS_EXPOSURES;
	values[0] = screen->white_pixel;
	values[1] = 0;
	xcb_create_gc(connection, background, native_window, mask, values);

	native_window = xcb_generate_id(connection);
	mask = XCB_CW_BACK_PIXEL | XCB_CW_EVENT_MASK;
	values[0] = screen->white_pixel;
	values[1] = XCB_EVENT_MASK_EXPOSURE | XCB_EVENT_MASK_KEY_PRESS;
	xcb_create_window(connection,
					  XCB_COPY_FROM_PARENT,
					  native_window,
					  screen->root,
					  0, 0,
					  250, 250,
					  10,
					  XCB_WINDOW_CLASS_INPUT_OUTPUT,
					  screen->root_visual,
					  mask, values);

	xcb_map_window(connection, native_window);
	xcb_flush(connection);

	// EGL Surface. In this case, a visible window

	EGLSurface window;
	EGLint windowAttribList[] =
	{
		EGL_RENDER_BUFFER, EGL_BACK_BUFFER,
		EGL_NONE
	};

	window = eglCreateWindowSurface(display, configs[0], native_window, windowAttribList);

	if (window == EGL_NO_SURFACE) {
		switch (eglGetError()) {
			case EGL_BAD_MATCH:
				std::cerr << "Bad Match!" << std::endl;
				break;
			case EGL_BAD_CONFIG:
				std::cerr << "Bad config!" << std::endl;
				break;
			case EGL_BAD_NATIVE_WINDOW:
				std::cerr << "Bad native window!" << std::endl;
				break;
			case EGL_BAD_ALLOC:
				std::cerr << "Bad Alloc!" << std::endl;
				break;
		}
		return 1;
	}



	// Simple XCB Event loop;
	while ((e = xcb_wait_for_event(connection))) {
		switch (e->response_type & ~0x80) {
			case XCB_KEY_PRESS:
				goto endloop;
		}
		free(e);
	}
	endloop:


	return 0;
}