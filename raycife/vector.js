var Vector = function (x, y, z) {
	this.x = x;
	this.y = y;
	this.z = z;
};

Vector.prototype.magnitude = function() {
	return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2) + Math.pow(this.z, 2));
};

Vector.prototype.scalarMult = function(k) {
	return new Vector(this.x * k, this.y * k, this.z * k);
};

Vector.prototype.dotProd = function(other) {
	return this.x * other.x + this.y * other.y + this.z * other.z;
};

Vector.prototype.crossProd = function(other) {
	return new Vector(this.y * other.z - this.z * other.y,
						this.z * other.x - this.x * other.z,
						this.x * other.y - this.y * other.x);
};

Vector.prototype.operate = function(operation, other) {
	return new Vector(operation(this.x, other.x),
						operation(this.y, other.y),
						operation(this.z, other.z));
};

Vector.prototype.add = function(other) {
	return this.operate(function(a,b) { return a+b;}, other);
};

Vector.prototype.sub = function(other) {
	return this.operate(function(a,b) { return a-b;}, other);
};

Vector.prototype.normalize = function() {
	var length = this.magnitude();
	return new Vector(this.x/length, this.y/length, this.z/length);
};