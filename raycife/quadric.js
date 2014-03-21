
var Light = function (direction, intensity) {
	this.direction = direction; // Vector
	this.intensity = intensity; // double
}

var Material = function (r, g, b, Ka, Kd, Ks, n) {
	this.r = r;
	this.g = g;
	this.b = b;
	this.Ka = Ka;
	this.Kd = Kd;
	this.Ks = Ks;
	this.specularExponent = n;
}

var Quadric = function(a, b, c, d, e, f, g, h, j, k, material) {
	this.a = a;
	this.b = b;
	this.c = c;
	this.d = d;
	this.e = e;
	this.f = f;
	this.g = g;
	this.h = h;
	this.j = j;
	this.k = k;
	this.material = material;
}

var Ray = function(origin, direction, depth) {
	this.origin = origin;
	this.direction = direction;
	this.depth = depth;
}