#ifndef PYOBJECT_HPP
#define PYOBJECT_HPP

#include <cmath>
#include <cstdint>
#include <memory>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

enum PyType { INT, FLOAT, BOOL, STRING, NONE, LIST, DICT, TUPLE };

struct PyObject;

namespace std {
template <> struct hash<PyObject> {
  size_t operator()(const PyObject &obj) const;
};
}

struct PyObject {
  PyType type;
  int pyInt;
  double pyFloat;
  bool pyBool;
  std::string pyString;

  std::shared_ptr<std::vector<PyObject>> pyList;
  std::shared_ptr<std::unordered_map<PyObject, PyObject>> pyDict;

  PyObject() { type = NONE; }

  PyObject(int val) {
    type = INT;
    pyInt = val;
  }

  PyObject(double val) {
    type = FLOAT;
    pyFloat = val;
  }

  PyObject(bool val) {
    type = BOOL;
    pyBool = val;
  }

  PyObject(const char *val) {
    type = STRING;
    pyString = std::string(val);
  }

  PyObject(std::string val) {
    type = STRING;
    pyString = val;
  }

  PyObject(std::vector<PyObject> val, PyType t) {
    type = t;
    pyList = std::make_shared<std::vector<PyObject>>(val);
  }

  PyObject(std::shared_ptr<std::unordered_map<PyObject, PyObject>> val) {
    type = DICT;
    pyDict = val;
  }

  bool isNumeric() const { return type == INT || type == FLOAT || type == BOOL; }

  int asInt() const { return type == BOOL ? pyBool : pyInt; }

  double asFloat() const { return type == FLOAT ? pyFloat : asInt(); }

  PyObject operator+(const PyObject &other) const {
    PyObject added;
    if (type == STRING && other.type == STRING) {
      added = PyObject(pyString + other.pyString);
    } else if (type == FLOAT || other.type == FLOAT) {
      added = PyObject(asFloat() + other.asFloat());
    } else if (isNumeric() && other.isNumeric()) {
      added = PyObject(asInt() + other.asInt());
    } else if (type == LIST && other.type == LIST) {
      std::vector<PyObject> result = *pyList;
      result.insert(result.end(), other.pyList->begin(), other.pyList->end());
      added = PyObject(result, LIST);
    } else if (type == TUPLE && other.type == TUPLE) {
      std::vector<PyObject> result = *pyList;
      result.insert(result.end(), other.pyList->begin(), other.pyList->end());
      added = PyObject(result, TUPLE);
    }
    return added;
  }

  PyObject operator-(const PyObject &other) const {
    PyObject substracted;
    if (type == FLOAT || other.type == FLOAT) {
      substracted = PyObject(asFloat() - other.asFloat());
    } else if (isNumeric() && other.isNumeric()) {
      substracted = PyObject(asInt() - other.asInt());
    }
    return substracted;
  }

  PyObject operator*(const PyObject &other) const {
    PyObject multiplied;
    if (type == FLOAT || other.type == FLOAT) {
      multiplied = PyObject(asFloat() * other.asFloat());
    } else if (isNumeric() && other.isNumeric()) {
      multiplied = PyObject(asInt() * other.asInt());
    } else if (type == STRING && other.type == INT) {
      std::string result;
      for (int i = 0; i < other.pyInt; i++) {
        result += pyString;
      }
      multiplied = PyObject(result);
    } else if ((type == LIST || type == TUPLE) && other.type == INT) {
      std::vector<PyObject> result;
      for (int i = 0; i < other.pyInt; i++) {
        result.insert(result.end(), pyList->begin(), pyList->end());
      }
      multiplied = PyObject(result, type);
    }
    return multiplied;
  }

  PyObject operator/(const PyObject &other) const {
    PyObject divided;
    if (isNumeric() && other.isNumeric()) {
      divided = PyObject(asFloat() / other.asFloat());
    }
    return divided;
  }

  PyObject operator%(const PyObject &other) const {
    PyObject modulo;
    if (type == FLOAT || other.type == FLOAT) {
      modulo = PyObject(std::fmod(asFloat(), other.asFloat()));
    } else if (isNumeric() && other.isNumeric()) {
      modulo = PyObject(asInt() % other.asInt());
    }
    return modulo;
  }

  PyObject operator-() const {
    PyObject negated;
    if (type == FLOAT) {
      negated = PyObject(-pyFloat);
    } else if (isNumeric()) {
      negated = PyObject(-asInt());
    }
    return negated;
  }

  bool operator==(const PyObject &other) const {
    if (type == STRING && other.type == STRING) {
      return pyString == other.pyString;
    } else if (type == NONE && other.type == NONE) {
      return true;
    } else if (isNumeric() && other.isNumeric()) {
      return asFloat() == other.asFloat();
    } else if ((type == LIST || type == TUPLE) && type == other.type) {
      return *pyList == *other.pyList;
    }
    return false;
  }

  bool operator<(const PyObject &other) const {
    if (type == STRING && other.type == STRING) {
      return pyString < other.pyString;
    } else if (isNumeric() && other.isNumeric()) {
      return asFloat() < other.asFloat();
    }
    return false;
  }

  bool operator!=(const PyObject &other) const { return !(*this == other); }

  bool operator>(const PyObject &other) const { return other < *this; }

  bool operator<=(const PyObject &other) const { return !(other < *this); }

  bool operator>=(const PyObject &other) const { return !(*this < other); }

  PyObject operator[](const PyObject &key) const {
    PyObject result;
    if (type == LIST || type == TUPLE) {
      result = pyList->at(key.asInt());
    } else if (type == DICT) {
      result = pyDict->at(key);
    }
    return result;
  }

  PyObject& operator++() {
    if (type == INT) {
      ++pyInt;
    } else if (type == FLOAT) {
      ++pyFloat;
    } else if (type == BOOL) {
      pyBool = true;
    } else {
      throw std::runtime_error("unsupported operand type for ++");
    }
    return *this;
  }

  PyObject operator++(int) {
    PyObject temp = *this;
    ++(*this);
    return temp;
  }

  PyObject& operator+=(const PyObject &other) {
    *this = *this + other;
    return *this;
  }

  friend std::ostream &operator<<(std::ostream &os, const PyObject &obj);

  std::vector<PyObject>::iterator begin() { return pyList->begin(); }

  std::vector<PyObject>::iterator end() { return pyList->end(); }

  explicit operator bool() const {
    switch (type) {
    case INT:
      return pyInt != 0;
    case FLOAT:
      return pyFloat != 0.0;
    case BOOL:
      return pyBool;
    case STRING:
      return !pyString.empty();
    case LIST:
    case TUPLE:
      return pyList && !pyList->empty();
    case DICT:
      return pyDict && !pyDict->empty();
    default:
      return false;
    }
  }
};

inline std::ostream &operator<<(std::ostream &os, const PyObject &obj) {
  switch (obj.type) {
  case INT:
    os << obj.pyInt;
    break;

  case FLOAT:
    os << obj.pyFloat;
    break;

  case BOOL:
    os << (obj.pyBool ? "True" : "False");
    break;

  case STRING:
    os << obj.pyString;
    break;

  case NONE:
    os << "None";
    break;

  case LIST: {
    os << "[";
    for (size_t i = 0; i < obj.pyList->size(); ++i) {
      if (i > 0)
        os << ", ";
      os << (*obj.pyList)[i];
    }
    os << "]";
    break;
  }

  case TUPLE: {
    os << "(";
    for (size_t i = 0; i < obj.pyList->size(); ++i) {
      if (i > 0)
        os << ", ";
      os << (*obj.pyList)[i];
    }
    if (obj.pyList->size() == 1)
      os << ",";
    os << ")";
    break;
  }

  case DICT: {
    os << "{";
    bool first = true;
    for (const auto &entry : *obj.pyDict) {
      if (!first)
        os << ", ";
      os << entry.first << ": " << entry.second;
      first = false;
    }
    os << "}";
    break;
  }
  }

  return os;
}
namespace std {
inline size_t hash<PyObject>::operator()(const PyObject &obj) const {
  switch (obj.type) {
  case INT:
    return hash<int>{}(obj.pyInt);
  case FLOAT:
    return hash<double>{}(obj.pyFloat);
  case BOOL:
    return hash<bool>{}(obj.pyBool);
  case STRING:
    return hash<string>{}(obj.pyString);
  case NONE:
    return 0;
  case TUPLE: {
    size_t combined = 0;
    for (const PyObject &element : *obj.pyList) {
      combined ^=
          hash<PyObject>{}(element) + 0x9e3779b9 + (combined << 6) + (combined >> 2);
    }
    return combined;
  }
  default:
    throw std::runtime_error("unhashable type");
  }
}
}

#endif // PYOBJECT_HPP
