# Case Study

An institution wants to develop an Attendance Management System, which offer different short course to the students. In previous one to two years, the student growth is tremendously increased. Currently they are using the manual system/excel based sheets for marking the attendance of their students. Now they are facing a lot of issues in maintaining the records and reporting to the center manager is at risk from the staff as they are unable to handle the file based system. They wants to hire you as a web developer to design, develop and successfully implement the system in their esteemed organization. Keep in mind that in every software development cycle, the requirement gathering is one of the most important step. Assume that the Centre Manager has done a meeting with your team, he/she has given you the requirement which are mentioned below:

Centre Manager states that:

-	We offer different courses in the institute (namely, Interactive Design and Multimedia, Slick Dot Net Development, Digital Media & Entrepreneurship)
-	Different teachers are hired by the institute to teach different courses in fixed time slots {Fixed Time means Like 2.5 hrs class twice a week from 7:00pm-9:30pm on Friday and Saturday or 5hrs class in a week from 10am-3:00pm}, a one teacher can teach same course but there is should be no clash between two classes.
-	A class can be comprise of many students (but limit it to 50 students per class/time slot)
-	Once a student registered in our portal by the institute staff, then whenever he/she wants to take another course from our institute. He/She do not have to register again. He/She will pay the fee and get enrolled in the course as per suitable time slot.
-	Now the major change they wants to do in marking of a student attendance is that; teacher itself will mark it. 
-	Teacher will login to the system, select the course of ongoing class, put the date of day and marked the students present one by one or mark absent.
-	There will be many formats of the report, which will only accessible to the Center Manager.
-	There is no need to add financial aspects in this system. A separate module will be create later.



pip install -r requirements.txt
```
# Getting Started
Create an .env file and define connection string of your database.
```bash
DATABASE_URL=(your connection string)
```

Run your application using,
```bash
uvicorn main:app --reload
```
`Note: --reload will allow your app to restart automatically on changes to the code`

Now go to `http://127.0.0.1:8000/docs` to see the automatic interactive API documentation (provided by Swagger UI).

`Work in progress`

# Important Links
Documentation: https://fastapi.tiangolo.com
