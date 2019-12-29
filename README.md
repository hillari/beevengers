
Hillari Denny
Ryan Richter
Raul Reutov 
CSCE A401 - Software Engineering
University of Alaska, Anchorage 

<h1>Alaska Beekeeping Society </h1>

><p>This website serves as a central location for people to get information about cold-weather beekeeping (particularly Alaska)</p>

Project specific changes to default Django:
 - A custom user admin has been implemented for this site (default Django User model has been extended).
  Most of this is configured in the users app. This also means you need to use the correct notation when 
  dealing with anything that references User (say for example, a store that keeps track of a users orders). 
  - Certain templates have been overridden in order to make changes to the admin page forms (ie change form, 
  submit line, etc.). These can be found in templates > admin > [appname]
  
 Miscellaneous Notes: 
  - This website does have a blog feature and all of the code/backend refers to it as such. However, the client requested
  the feature be called "Articles", so any reference to this on the front end will be "articles" and not "blog".
  - The current implementation of the store is not a fully functioning e-commerce store. Instead, an site-user can create 
  an order which gets stored as a database entry in the form of an order request. These can then be viewed from the user
  admin page. This "pseudo store" was designed to be standalone (it it does not have relationships with any other table).
  The idea is that a future developer can easily implement an e-commerce app without having to mess with an existing schema.
  We hoped to make the life of any future dev as easy as possible, please dont hurt us =)
  - The current deployment should include a custom user with limited permissions in the user admin page. This is to
  simplify the end-user experience as much as possible. Classes that aren't necessary for the end-user to write a blog
  post or manage a product need not be included when specifying permissions for this user (ie groups, users).
  - A subscription system that is fully functional is included but at the time of this writing the client did not
  wish for this to be live yet. Therefore, the code for it has been commented out. Ideally, this could me moved to an
  app of it's own (it is currently part of the homepage).
 
  
  Unfinished business:
  - There were some things out group could not get to simply due to time. One of these things is how the server will 
  store images. The project is set up to store images appropriately. However, if a product or blog with an associated
  image is removed, the image is not removed from the server. 
  - Ideally, the custom user admin could be further extended to allow the end-user to create and modify additional 
  pages outside of the blog and store. 
  - It would be helpful to include a rich-text editor for the blog at some point, to make end-users life a bit easier.
  - There are some unit tests included (blog, users apps). These may need some modification to be ran on the developers
  machine. 
  
  
<h3>Technologies:</h3>
<ul>
<li> Bootstrap 4.x.x </li>
<li> Python 3.7.4 </li>
<li> Django 2.2.6 </li>
</ul>

