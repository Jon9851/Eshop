**_Eshop_**

WELCOME TO Eshop

Welcome to Eshop an online e-commerce store which server as your one stop shop for all your tech needs. There are plans to add products to our already growing inventory very soon. This online store was created using Django frameworks and PostgreSQL to manage the inventory database. The shop features a secure checkout payment with stripe payments which links in to the user profile and a complete order history included on the profile page. Eshop has many more features which will included down below.

Eshop<a href="https://eshopms4.herokuapp.com/" target="_blank" rel="noopner">Game Review</a>



![Games Review responsiveness ](gamesreviewc/static/image/responisvems3.png)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
   * [User Stories](<#user-stories>)
   * [**Wireframes**](<#wireframes>)
   * [**Design Choices**](<#design-choices>)
       * [Color Scheme](<#color-scheme>)
   * [**Features**](<#features>)
       * [Home](<#Home>)
       * [Game](<#Game>)
       * [Publishers](<#Publishers>)
       * [Titles](<#Tiles>)
       * [Reviews](<#Reviews>)
       * [Profile](<#Profile>)
       * [Werkzeug](<#Werkzeug>)
       * [Defensive](<#Defensive>)
       * [Data Schema](<#Data-Schema>)
* [**Future Features**](<#future-features>)
* [**Technologies Used**](<#Technologies-Used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Content**](<#content>)
* [**Future Features**](<Future-Features>)
* [**Acknowledgements**](<#acknowledgements>)                

# User Experience (UX)

## User stories

 ### Motivation for creating an E-commerce store
 The main Motivation for creating an E-commerce store was, is that when shopping online for tech information I find it difficult to choose as there to many distractions and adverts on these sites trying to promote you to buy stuff. Eshop is a simple e-commerce store with best products on the market available for you!

 The target audience for this site are, people that tired of these big online stores, trying to sell you stuff you don’t want or stock they can’t sell. Eshop has the best products available to buy at best prices for people that don’t want to spend loads of money but still want the best tech on the market today. 

 Eshop was designed with security in mind. From the secure checkout, and to pages that have restricted access for the users to keep their information safe, such as the wish list and user profile including delivery information and a complete order history available so why not shop today. 


 ### First time Visitor Goals 
1. All available products in separate categories  
2. All products have detailed description 
3. The amount of products available on the page
4. Easy user interface 
5. Search bar 
6. Order conformation
7. Secure site with card payment
8. User profile with order history. 

 ### Returning Visitor Goals   
1. Login and registration features available
2. Password recovery  
3. Images and text have links to the product description
4. Order history 
5. A feature to save personal information and delivery information 
6. Be able to save future purchase to your profile 
 
 ### Admin Privileges  
1. Be able to add product easily without editing the source code  
2. Product form to edit and delete product inventory. 
3. Be able to add new products to the product database easily and quickly
4. Be able to add to staff to the database with admin access
5. Admin access to view all customers that use Eshop


# Wireframes
The wire-frames for ‘Games Review’ were produced in[Balsamiq](https://balsamiq.com).
There are frames for a full width display ( 1920 x 1080 package)and a small mobile 
device (360 x 640). The final site varies slightly from the wire-frames due to bugs and design 
changes during development that occurred during the creation process. Mobile wire-frames haven`t been included due to the use of Materialize as this
includes integrated  responsiveness package.

 

![Wireframe Desktop]
![Wireframe Desktop]
![Wireframe Desktop]

[Contents](<#contents>)

# Design Choices
 When designing the games review database I wanted it to be to be simple to use, as I wanted the CRUD functionality to be present in the database . Games review contains 13 pages which 11 pages related to Crud functions with in the database. After spending serval hours looking at Materialize i eventually decided on cards, collapsibles and a nav bar with a built in side nav bar for the design. I wanted the overall look of the side to feel simple and easy to use. All pages are linked up with either url`s or with buttons directing you to the different pages on the site.

 The nav bar covers all 13 pages of the site which is kept on the base template, across all the pages i have put in a background image which gives the site a nice contrasts from the text on the page. Early on in the design I knew i was going to use green for the overall look of the site, I originally choose blue for the text, but due to it being difficult to see I changed the text color scheme to white which stood out more. 

The game page was designed to give users ideas of games ideas that they can input into the database. All the images on the games page are for educational purposes only.
The design for the page comes from materialize cards which i edited the background to white and the text to a dark green color.

During the final stages of development I choose to lock out users from deleting publishers as this ties all the relational database together. I wanted to give the uses so feed back and warning messages so i choose to implement flash messages.
 

![Hex Colors ](gamesreviewc/static/image/hex3.png)
 
 
 THe colors that where chosen  are displayed in image above.

 Green darken 2 #388e3c was used for the nav bar footer and other elements with in the site

 Green darken 4 #1b5e20 was used for the text on the games page so the text would stand out. 
 
 White was used for a few various things backgrounds and text and flash messages.

 The buttons colors are red black and yellow.

  

[Contents](<#contents>)

# Features
### Home 
The home page features a nav bar which has lock function depending on whether you are logged or out. Below the nav bar you have a text slider with quotes from different video 
games, and below that you have and image slider with four different games images combined in to a single changing image, and a footer which covers all 13 pages. The image slider positioning is a small bug as it appears differently on different devices.
![Home](gamesreviewc/static/image/homegr.png)

### Games
The game page features cards from materialize with different games images and a brief description of them.
![Game]

### Publishers
The publishers page is the key part of the database as you cant add anything in till you first add a publisher. The publishers page features a fully functioning Crud system with edit and delete
buttons but only admin can delete publishers.The publishers page also provides links to the add and edits pages so you user can edit if they change there minds.

![Publishers]


### Titles
The titles pages is where you can add games to the site, the titles page features collapsible with the publisher names on the drop and in the drop down there is review, edit and delete buttons to give the user full access. The buttons provides links to the review page and edit games page. Users can delete games as they wish with a flash message appearing to warn them about deleting the games.

![Titles]


### Reviews
The Review pages is where you can add reviews to the site, the reviews page features collapsibles
 with the game names on the drop and in the drop down there is edit and delete buttons to give the user full access. The buttons provides links to the review page and edit games page. Users can delete reviews as they wish with a flash message appearing to warn them about deleting the reviews. (bug game name wont appear i left out the jinja syntax for this reason)

![Reviews]

### Profile
The profile pages displays the use login details once they have registered on the site with a flash message.
the login and register page are very Similar the only differences are the text on the pages. The login and register pages are very simple in there design. 

![Profile]

#### Data Scema 

The image below details my database schema on how all my relationships within my database are connected and. 

![Data-Schema]


[Contents](<#contents>)

## Deployment

  ### **Deployment**

 This project was deployed to heroku and the steps to do this are below:

1. sign up and log into heroku
2. In the top right hand corner of the heroku website click new, then create new app
3. Name app and select region
4. click create app
5. Install postgres under the resources tab
6. Insert relevant config vars into heroku, such as IP,PORT,SECRET_KEY, DATABASE_URL
7. You can click connect to github but this project used the CLI method.
8. Log into heroku via CLI
9. Create a git remote for heroku
10. Push all changes to the staging area
11. Push to heroku for your app to run and function.
 
 # Technologies Used
   
* [HTML5](https://html.spec.whatwg.org/) -Used to create the contents and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) -Used to create the styling.
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)) Used to create the routes
* [Balsamiq](https://balsamiq.com/wireframes/) - Used to create the wire-frames.
* [Gitpod](https://www.gitpod.io/#get-started) - Used to deploy the website.
* [Github](https://github.com/) - Used to host and edit the website code.
* [Code Beautify](https://codebeautify.org/jsvalidate) - To test and run the code
* [W3 Schools](https://validator.w3.org/)- To test the html and css code.
* [JavaScript (ES6)](https://open-vsx.gitpod.io/vscode/item?itemName=xabikos.JavaScriptSnippets)
* [ami responsive design](http://ami.responsivedesign.is) - To test out responsiveness on all devices
* [heroku](https://www.heroku.com) - Used for deployment
* [mongodb](https://www.mongodb.com) - Used for the user db 
* [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) User for the publisher games and reviews db 
* [PEP8 Online Checker](http://pep8online.com/) Use to check python routes
* [Materialize](https://materializecss.com/) Used to create html templates



[Contents](<#contents>)

# Testing
 Please refer to [**Testing **](testing.md) for more information on testing 'Quiz Of The World'.
  
  # Clone  Repository
   To Clone a repository use the following steps to guide you through it.
   1. Under the repository’s name, click on the code tab.
   2. click on the clipboard icon to copy the given URL.
   3. In your IDE of choice, open Git Bash.
   4. Change the current working directory to the location where you want the cloned directory to be made.
   5. Type git clone, and then paste the URL copied from GitHub.
   6. Press enter and the local clone will be created.

   ![clone Image ]




[Contents](<#contents>)

### Credits
1. W3schools- I used their tutorials on HTML and CSS for further understanding and troubleshooting  throughout my project.
2. Stack Overflow- I used Stack Overflow to get a more in depth understanding on HTML and CSS throughout my project.
3. Code Institute Example of the READ.MD- I used these as template when planning and writing my README file.
4.Code Institute tutors that helped me during my project.

[Contents](<#contents>)

# Acknowledgements
 
 The site was cerated for my milestone project 3 for the [Code Institute](https://codeinstitute.net/) Full Stack Software Developer diploma. I would like to thank all the tutors at the code institute for their help during the development of my first milestone project. I would also like to thank [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his guidances and help as his feedback was extremely key in completing my third milestone project.
 Brain Codex for help during the creation process. 