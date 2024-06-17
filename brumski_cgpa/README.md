# A CGPA calculator python library created in C++.

1. a. This library is a python-only library that was made using C++ and a C++/Python interoperability library named "pybind11". 

   b. To use this library, simply download it to your project directory and type *import brumski_cgpa* in your python file.

2. Functions in this library include: 

   *brumski_cgpa.getInput()* is the python does what float(input()) and int(input()) do plus it enters into an infinite loop until the user enters a double or int.

    *brumski_cgpa.grade_calc(a)* converts an int or double into a grade (A-F). *a* represents the double/int. It returns the type "str". E.g grade: str = brumski_cgpa.grade_calc(a).

    *brumski_cgpa.grade_point(g, u)* gets the grade point for a particular course. *g* is the grade (A-F) and *u* is that course's units. It results the type "double". E.g grade_point: float = brumski_cgpa.grade_point(g, u).

3. Choose the .so version of the library if you're on Linux/Android, choose the .dll if you're on Windows. As of Jun 5, 2024 the .dll file isn't released yet.

4. Created by David Tamaratare Oghenebrume, a Computer Engineering student and C++ enthusiast.
