# Module-Dashboard
A simple GUI interface to view and manage modules and grades

ccccccccccc  qqqqqqqqqqq  yyy      yyy      aaaaa          oooooooooooo
ccccccccccc  qqqqqqqqqqq   yyy    yyy      aaa aaa         oooooooooooo
ccc      cc  qq       qq    yyy  yyy      aaa   aaa        oo        oo
ccc          qq       qq     yyyyy       aaa     aaa       oo        oo 
ccc          qq       qq      yyy       aaaaaaaaaaaaa      oo        oo
ccc      cc  qq       qqq     yyy      aaaaaaaaaaaaaaa     oo        oo 
ccccccccccc  qqqqqqqqqqqqq    yyy     aaa           aaa    oooooooooooo
ccccccccccc  qqqqqqqqqqq qq   yyy    aaa             aaa   oooooooooooo

The idea behind this project is to create a GUI interface in which the user can add module into a Pandas database. Currecntly, the features are limited to adding modules into the database and viewing the database in whole. Planned features include searching for subject by code, filtering by grade (where grade <= 50, for example), and calculating the WAM. 

How to use this program: 
1. Download "pandas.csv" and "subjects_database.csv" and move into the same directory as "ModuleDashboard.py".
2. Run the program with cmd or terminal using "python ModuleDashboard.py".
3. Type in subject code (example, "csit128") and press the search button.
4. If there is a subject with that code in the database, the subject name field will be updated.
5. Proceed to add grade and then click the add button. The subject is now added into the database.
6. Note: The subject code can be typed in upper or lowercase, it doesn't matter.

**Bugs and features should be kept in a separate changelog file.**
