# ERM-system
## _Employer_ Relationship Management system for job seekers who intend to land their dream job
### Plan

1. List of the features:
    1. Basic form that allows users to enter the details of each job application:
        - date of application, 
        - company, 
        - position, 
        - status (whether there was a response, interview, etc.);
    2. Search function that allows users to search through their previous job applications by keyword or date range;
    3. Dashboard that displays statistics about the user's job search efforts, such as:
        - number of applications submitted, 
        - the percentage of responses received, 
        - and the average time to receive a response;
    4. Notification system that reminds users to follow up on their applications if they have not received a response within a certain time frame;
    5. Export system: allow users to export their job search data to a spreadsheet or PDF for easy sharing and record-keeping.


~~2. Create a Django project and set up the virtual environment to isolate the dependencies.~~

3. Create the database schema for the app using Django's ORM. Define necessary models.

4. Implement the authentication system.

5. Implement the core functionality.
 
6. Develop the frontend of the site using HTML, CSS, and JavaScript. Use a frontend framework such as React or Vue.

7. Implement any additional features: user profiles, search and filtering, ratings and reviews.

8. Add list of used tekhnologies.

9. Add documentation.

10. Test the app thoroughly and deploy it to a web server or cloud service provider.

### RU:
*Концепция проекта*
Сайт, который помогает человеку, который ищет работу - отслеживать свои усилия (предпринятые действия) на этом пути. 

Каждая сущность БД - отдельная итерация по взаимодействию с потенциальным работодателем.

При отправке резюме - фиксируется дата отправки, компания, позиция, версия резюме, использованный шаблон, текст сопроводительного письма, был ли отклик, было ли тестовое (если да, то ссылка на репозиторий с решением), было ли интервью (созвон, - онлайн, - оффлайн), был ли оффер. С кем общались (ФИО, контакты).

Возможные сценарии использования:
⁃ Изучена новая технология, обновлено резюме - отправляем обновлённое резюме всем, кому до этого отправлялась предыдущая версия;
⁃ После неудачного интервью - проведена работа над ошибками; отправляется обновлённое резюме, сопроводительное письмо;
⁃ В портфолио добавлен новый проект - рассылка резюме всем, кто есть в базе с информированием о своём достижении;
⁃ Фиксируются предпринятые усилия по поиску работы.

Использование сайта помогает реализовать так называемый системный подход при поиске первой работы и при дальнейших поисках (когда появляется желание и/или необходимость сменить работу).

Сайт может быть полезен любым соискателям: в любых сферах деятельности.

Даёт возможность гибко анализировать объём и качество проделанной работы; в том числе - визуализировать полученные результаты.

Это, своего рода, мини CRM-система, где в роли клиентов - контрагенты потенциальные работодатели.

Каждый отклик - новая итерация. Ей соответствует отдельная страница с метриками. 
На главной странице представлена общая таблица; есть возможность провалиться в каждую итерацию.

### Автор: Илья Корепанов, ikorepanov@gmail.com

### EN:
*Project concept*
A site that helps a person who is looking for a job - track their efforts (actions taken) along the way.

Each database entity is a separate iteration of interaction with a potential employer.

When sending a resume, the date of sending, company, position, version of the resume, template used, text of the cover letter, whether there was a response, whether there was a test (if yes, then a link to the repository with the solution), whether there was an interview (phoned, - online, - offline), whether there was an offer. Who did you communicate with (name, contacts).

Possible use cases:
⁃ New technology explored, CV updated - we send the updated CV to everyone who previously received the previous version;
⁃ After an unsuccessful interview - work was done on the bugs; send an updated resume, cover letter;
⁃ A new project has been added to the portfolio - sending resumes to everyone who is in the database with information about their achievement;
⁃ Efforts made to find a job are recorded.

Using the site helps to implement the so-called systematic approach when looking for the first job and in further searches (when there is a desire and / or need to change jobs).

The site can be useful to any applicants: in any field of activity.

Gives you the opportunity to flexibly analyze the volume and quality of the work done; including visualization of the obtained results.

This is, in a way, a mini CRM-system, where potential employers are counterparties in the role of clients.

Each response is a new iteration. It has a separate page with metrics.
The main page contains a general table; it is possible to fall in to each iteration.

### Author: Ilia Korepanov, ikorepanov@gmail.com