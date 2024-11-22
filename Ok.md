### Question: Define Encapsulation 
**Answer:** Encapsulation is an Object-Oriented Programming (OOP) concept that binds data (variables) and functions (methods) together into a single unit, usually a class, while restricting direct access to some components using access specifiers like `private`, `protected`, and `public`. It ensures data security and abstraction. 

**Example:** 
```
class Car { 
    private: int speed; 
    public: void setSpeed(int s) { speed = s; }
    int getSpeed() { return speed; } 
};
```
### Question: What is Inline Function? 
**Answer:** An inline function is a function whose definition is expanded in place at the point of invocation rather than being called through normal function call mechanics. 

**Example:** 
```
inline int add(int a, int b) { return a + b; }
```
### Question: What is Class? Give Its Syntax 
**Answer:** A class is a blueprint for creating objects in C++. It defines the properties (attributes) and behaviors (methods) that objects of the class will have. 

**Example (Syntax):** 
```
class ClassName { 
    private: int attribute1; // Private members 
    public: void method1(); // Public members 
};
``` 

### Question: What is Constructor? 
**Answer:** A constructor is a special member function of a class that initializes objects when they are created. It has the same name as the class and no return type. 

**Example:** 
```
class MyClass { public: MyClass() { 
    // Constructor 
    cout << "Constructor called"; 
};
``` 

### Question: Explain Any Two Uses of Scope Resolution Operator (`::`) 
**Answer:** 1. To access global variables when a local variable of the same name exists. 2. To define class methods outside the class body. 

**Example:** 
Access global variables: 
```
int x = 10; 
void func() { int x = 20; cout << ::x; // Access global x } 
```
Define methods outside the class body: 
```
class MyClass { void display(); }; 
void MyClass::display() { cout << "Hello"; }
```
### Question: List the Operators Which Cannot Be Overloaded  
**Answer:** 
    1. Scope resolution operator (`::`) 
    2. Member selection operator (`.`) 
    3. Pointer-to-member operator (`.*`) 
    4. `sizeof` operator ### Question: 

### What is Virtual Function? 
**Answer:** A virtual function is a member function in a base class that you can override in derived classes. It supports run-time polymorphism by resolving the function call at runtime. 

**Example:** 
```
class Base { 
    public: virtual void display() { cout << "Base class"; } 
};
```

### Question: What is Stream? 
**Answer:** A stream is a flow of data from a source to a destination. - Input Stream (e.g., `cin`): Used for reading data. - Output Stream (e.g., `cout`): Used for writing data. 

**Example:** 
```
int x; 
cin >> x; // Input stream 
cout << x; // Output stream 
```

### Question: Explain `get()` and `put()` Functions 

**Answer:** - `get()`: Reads a single character from the input stream. - `put()`: Writes a single character to the output stream. 

**Example:** 
`get()` Example: 
```
char c; 
cin.get(c); 
cout << c;
```
`put()` Example: 
```
char c = 'A'; 
cout.put(c); 
```

### Question: What Are the Access Specifiers Used in C++? 
**Answer:** 
    1. `public`: Members are accessible from anywhere. 
    2. `protected`: Members are accessible within the class and derived classes. 
    3. `private`: Members are accessible only within the class. 
    
    **Example:**
   
   ```
    class Example { 
        private: int a; // Private 
        protected: int b; // Protected 
        public: int c; // Public 
    };
   ```
