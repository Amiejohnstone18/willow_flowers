# Willow Flowers 

--> image of website on different devices 

Willow Flowers is a user-friendly e-commerce website built via main technologies [HTML](https://html.com/), [CSS](https://en.wikipedia.org/wiki/CSS), [JavaScript](https://www.javascript.com/about), [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/). 
The purpose of this website is to enable consumers to purchase items, such as plants and flowers, and create a user profile to store their previous orders and site favourites to access at any time. The website owner can upload, edit and delete products when necessary. 

# Contents
* [UX Design](#UX-Design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](##Skeleton)
    * [Surface](#Surface)
    * [Wireframes](#Wireframes)
* [Project Review](#Project-Review)
* [Databse](#Database)
* [Trello](#Trello)
* [Code Structure](#Code-Structure)
* [Features](#Features)
    * [Existing Features](#Existing-features)
    * [Features Left to Implement](#Features-Left-to-Implement)
* [Technologies Used](#Technologies-Used)
    * [Other Tools](#Other-Tools)
* [Testing](#Tesing)
* [Deployment](#Deployment)
* [Credits](#Credits)



# UX Design 

## Strategy
Following the five planes of user experience design, the strategy has been separated into *Who*, *What*, *Where*, *When* and *Why* to initially  understand the website users’ requirements and needs. 

**Who** - The customer will be an individual looking to purchase flowers or a plant for an occasion such as a Birthday, New Baby, Congratulations, Wedding, Get Well Soon and inside out outside plants. The website will therefore not have a specific target demographic. 

**What** - The idea for this website is to design and build an e-commerce florist site whereby consumers can purchase and have products from the site delivered to recipients depending on the occasion at hand. They are also able to favourite specific items and keep them in their personal account favourites to revisit later. 

**Where** - The site will promote all products available, along with links to social media platforms to showcase to a wider audience. The site will also include a contact page, whereby consumers can contact the owners with any queries they have. 

**When** - The website will be available for users to make a purchase at any point in their journey, however, it will also provide information about order cut offs for expected delivery dates and times. 

**Why** - Consumers will want to use this website to purchase florist products due to its easy navigation and information architecture layout, and simple payment process.

Following this, I also conducted some user stories to ensure the website will serve its purpose.

| As a:       | I would like to:                                | So that I can:                                            |
| :---        | :----                                           |  :---                                                     |
| **User**    | Shop the florist range by occasion              | Purchase some flowers for a particular event              |
| **User**    | Create a user account                           | Keep track of my previous purchases                       |
| **User**    | Search for a particular flower                  | Order them for a specific occasion                        |
| **User**    | Add multiple products to my basket              | Order more than one item at once                          |
| **User**    | Add and delete items from my basket             | Decide on my final purchase at the end of my experience   |
| **User**    | Receive an email confirmation of my order       | Have a copy of my order number and expected delivery      |
| **User**    | Favourite an item advertised on the site        | Come back to it and purchase later.                       |
| **User**    | Contact the owners of the business              | To thank them for my purchase                             |

<br>


| As a:       | I would like to:                                | So that I can:                                |
| :---        | :----                                           |  :---                                         |
| **Admin**   | View a list of orders that have come through    | Process the orders                            |
| **Admin**   | Add, Update, and delete products                | Update the website when necessary             |
| **Admin**   | Receive a copy of any contact forms submitted   | So, I can respond accordingly to the customer |




## Scope
The features included in this website will consist of:
* The option to narrow down a product search through filtering the occasion. 
* A search page to pull up results based on name and description (through a term such as a colour).
* Personal login to view previous orders.
* An option to sign up as a website user- to complete a purchase or save items to your favourites.
* Shopping basket to display reserved items and a subtotal amount (£).
* Testimonials from previous customers.
* Online payments and order confirmation.

## Structure 
Information architecture will be organised via product information. Bootstrap cards will be used to organise the product preview images on pages such as the search, the product pages and the basket to keep the layout clean and simple. Buttons will guide the user to complete their purchase, sign up, login or navigate to another page on the site. 

## Skeleton
The navigation menu will be divided like so:

![Nav-links-menu](documents/images/nav-links-menu.png)

## Surface
Due to the fact there will be a lot of bursts of colour through the imagery of the products, I thought it would be best to keep surrounding colours minimal as to not over-crowd the page and avoid distraction for users. I will use an accent colour of Bubble-gum Pink (#ffc1cc) for the navigation menu, footer and buttons. The font used will be [Playfair Display](https://fonts.google.com/specimen/Playfair+Display?query=playfair), taken from [Google Fonts](https://fonts.google.com/).

## Wireframes 
Below is a preview of the Home Page wireframes for desktop, tablet and mobile created on [Balsamiq](https://balsamiq.com/). The individual desktop, tablet and mobile wireframes with all pages can be found [here](documents/wireframes).

![wireframes-preview](documents/images/wireframes-preview.png)


[Contents](#Contents)

# Project Review 

I constantly reflected through my wireframes during the development process for this project. Upon project completion, there are a few features which I refrained from implementing or changed during the development. 

**Toast Notifications**  – After much consideration, I had decided to not include toast messages into the final project. This was because I felt they weren’t completely necessary for the project at this stage. This is potentially something I will look to include further along the line of developing this project. 

** Wireframe Image 

**The Basket Icon** – When it came to adding items to a user’s basket, initially I had designed for this to be done via clicking on a basket icon displayed in the product’s full description. I found out through my development that this was not actually the most feasible way to add an item to a user’s basket due to the quantity factor.

** Wireframe Image 

**Testimonial Carousel** - Initially I had designed this to show two rotating customer testimonials at a time on the Home page. This initially caused issues as the testimonials would only show inside the left column, leaving the right blank. Due to this, after careful consideration, I had decided to only preview one testimonial at a time on the home page, spanning the full width of the page.

** Wireframe Image 

[Contents](#Contents)

# Database
The database used for the development of the project was SQLite which was later moved to Heroku using the Postgres add-on. Below is a visualisation of the database schema.

** Database Schema Image

[Contents](#Contents)

# Trello 
To ensure I was staying organised and keeping in time with the deadline for this project, I created a Trello Board to list things I needed to do, were a working progress and what was completed. This helped me to ensure I was covering all aspects of the requirements for this project. 

** Insert Trello Board Image 

[Contents](#Contents)

# Code Structure

** Image of code structure 

[Contents](#Contents)

# Features

## Existing Features 
*	Logo – The logo appears consistently on every page in the top left corner. Once clicked, this will also direct the user back to the Home page of the website. 

** IMAGE

*	Favicon -  The Favicon displays in the user’s browser. Should the user move to another tab, they can recognise from the favicon the Willow Flowers branding and direct back to the browser. 

** IMAGE

*	Icon Navigation – The top right corner of the website provides icon navigation links to Favourites, User Login, Basket and Search. These are visually accessible on every page allowing the user to quickly navigate to the required page.  

** IMAGE

*	Navigation Menu – The main navigation menu provides links to the Home page, a dropdown to the Flower products and Plant products, and a link to the Contact form. On a mobile view, these can be accessed via the responsive navigation bar. 

** IMAGE

*	Contact Form – Allows users to contact Willow Flowers directly by having them fill out a contact form which requires their name, email address and a message to submit.  

** IMAGE

*	Customer Testimonials  - These can be found at the bottom of the home page and are used encourage new consumers to purchase products from the site based on previous customer experiences. 

** IMAGE

*	X3 Image links – On the home page is three circle images which provide links to the categories Birthday, Inside Plants and Wedding. When an image is clicked the user will be taken to that products category of items displayed as product cards. 

** IMAGE

*	Product Cards – While browsing product categories, users will be presented with product cards. These will provide brief information on an items name, image, and price with a button to “view more” which will take the user to that product’s full description. 

** IMAGE

*	Search Functionality – This will be found in the navigation menu and will take a user to a page whereby they are able to enter a word based on a product they would like to find. From here a list of products resulting to that search term will be displayed.

** IMAGE

*	Links to Social Media – Links to Instagram, Twitter and Pinterest are accessible in the bottom right of the page footer. These links will take a user directly to the social platforms in a new browser, to ensure they don’t venture off from Willow Flowers. 

** IMAGE

*	User Profile– Users have the option to create a personal profile whereby they can login and have access to their previous orders. The user will have to click on the user icon at the top of the page and then either login or sign up to create an account. 

** IMAGE

*	Favourite Items – The favourites features allow users to essentially save an item for later. To add a product to their favourites, a user would have to click on a products full description and click on the heart to add it to their list of favourites. A user can access this list at anytime by clicking on the heart in the top right icon navigation. If there are no items to display in the Favourites, the user will be presented with a message “No items in your favourites” and a button leading them back to the Home page. 

** IMAGE

*	Add Items to Basket – For a user to complete a purchase on a product, they would be required to add that item to their basket. This can be completed by selecting the quantity required on the items full description and selecting “Add to basket”. 

** IMAGE

*	Update Basket - The basket icon displayed in the top right corner will take the user to a list of items currently in their basket. To add or remove quantities from their basket, the user would manipulate the quantity arrows next to each product and select “Update Basket”. 

** IMAGE

*	Checkout – To complete a purchase the user would be required to browse to their basket and click “Checkout”. They will be taken to a page whereby if they are a logged-in user, their personal information will be auto filled out. If not, the user will be required to fill in the necessary personal fields, along with their payment information. This was built using Stripe Payments. 

** IMAGE

*	Checkout Confirmation – Upon completion of purchase, the user will be directed to a checkout confirmation page, informing them of where the email address their confirmation has been sent to along with their order confirmation number. 

** IMAGE

*	Admin Profile – The Amin profile is created for the site superusers. The Admin view provides different access links and visuals to a standard user. By clicking on a product, they can update product information or delete the product from the website. In the Admin profile, the Admin can upload new products to the website by filling out the required information. 

** IMAGE

*	View Products by Category – The website provides users to browse specific categories of products. By clicking on either “Flowers” or “Plants” in the navigation menu, the user can browse all products available or select the specific category each product falls under. 

 ** IMAGE


## Features Left to Implement

*	Live chat – Allow users to chat online with Willow Flowers to get a direct and fast response on their query.
*	About Us – Provide some information about how Willow Flowers was initially created and who are the employees involved, to give the website a more personal touch. 
*	Subscription Offer – Whereby a user can pay a monthly fee and receive a random product from Willow Flowers every month.
*	Contact Information - Provide information such as phone number, address and business hours in the far left of the Footer to display on every page. 
*	GDPR Feature- Allowing the user to opt-in to receiving promotion email offers from Willow Flowers. 
*	Review System – Give users the option to review products on a star rated system based off their personal experience with the product. These would be visible on the product cards. 
*	Toast Notifications – Previewing a brief message to users when they have complete certain actions on the website.

[Contents](#Contents)

# Technologies Used
*	[HTML]() – Used as the main language for the templates.
*	[CSS]() – Used to style the website.
*	[JavaScript]() – Used for some frontend functionality.
*	[Python]() – Used for backend data manipulation.
*	[Django]() – Used to enable rapid development to create a secure and maintainable website. 
*	[Bootstrap]()- Used HTML	 and CSS templates to feature on the website, along with some JavaScript plugins.
*	[Pillow]() – Used to add images to the database.
*	[Allauth]() – Used to create user authentication, registration, and account.
*	[Gunicon]() – Used to server Django Python applications through WSGI interface on production.
*	[db.sqlite3]() – Used to hold the database while in development. 
*	[PostgreSQL]() – Used to store the primary data after deployment. 
*	[Git]() – Used for version control.
*	[GitHub]() – Used to store my project repository.
*	[GitPod]() - Used to build the development of the website.
*	[Heroku]() – Used to host the website.
*	[Stripe]() – Used to process payments on the website. 
*	[AWS]() -
    *	[S3]() – Used to store and retrieve data.
    *   [IAM]() – Used for security.
*	[Webhooks]() - Used to allow the web applications to communicate.
*	[Google Fonts]() – Used for website typography.
*	[Font Awesome]() - Used for icons.
*	[Crispy Forms]() – Used to create forms for the website.

# Other Tools 

*	[Adobe illustrator]() - Used to create the logo and favicon.
*	[Balsamiq]() – Used to create the wireframes.
*	[Grammarly]() - Used to check spelling and grammar.
*	[W3C Markup]() - Used this to check my HTML for errors and typos.
*	[W3C CSS]() - Used this to check the validity of my CSS.
*	[Jshint]() – Used to check my JavaScript code.
*	[pep8online]() – Used to validate my Python code.
*	[dbdiagram]() – Used to initially format my database schema


[Contents](#Contents)

# Testing 

[Contents](#Contents)

# Deployment 

[Contents](#Contents)

# Credits 

[Contents](#Contents)
