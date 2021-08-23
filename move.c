#include <Python.h>
#include <math.h>

typedef struct {
	float x;
	float y;
	float yaw;
} basic_coord;

basic_coord basic = {0, 0, 0};

basic_coord update(float time)
{
	basic_coord tmp = {};

	tmp.x = sinf(time) * 2500;
	tmp.y = cosf(time) * 2500;
	tmp.yaw = time * 0.4;

	return tmp;
}


static PyObject* update_coord(PyObject *self, PyObject *args)
{
	float time;

	if(!PyArg_ParseTuple(args, "f", &time))
	{
		return NULL;
	}

	basic = update(time);

	Py_RETURN_NONE;
}

static PyObject* get_x(PyObject *self, PyObject *args)
{
	return PyFloat_FromDouble((double)basic.x);
}

static PyObject* get_y(PyObject *self, PyObject *args)
{
	return PyFloat_FromDouble((double)basic.y);
}

static PyObject* get_yaw(PyObject *self, PyObject *args)
{
	return PyFloat_FromDouble((double)basic.yaw);
}

static PyMethodDef MoveMethods[] = {
	{"update_coord", (PyCFunction)update_coord, METH_VARARGS, "move1: update_coord"},
	{"get_x", (PyCFunction)get_x, METH_NOARGS, "move2: get_x"},
	{"get_y", (PyCFunction)get_y, METH_NOARGS, "move3: get_y"},
	{"get_yaw", (PyCFunction)get_yaw, METH_NOARGS, "move4: get_yaw"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef movemodule = {
	PyModuleDef_HEAD_INIT,
	"move",
	NULL,
	-1,
	MoveMethods
};

PyMODINIT_FUNC PyInit_move(void) {
	return PyModule_Create(&movemodule);
}

