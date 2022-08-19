* [**Testing**](<#testing>)
* [**Manual Testing**](<#manual-testing>)
* [**Bugs**](<#bugs>)
* [**Accessibility**](<#accessibilty>)
# Testing
W3C markup validator and W3C CSS validator were used to test and validate all the code on all 4  pages of history quiz to ensure that there were no syntax errors. JS hint was used to test the Javascript and PEP8 online checker for python errors.

 # index
The image below is testing for the index.html file, only javascript causing warnings. 

![Testing on W3C Html](documentation/testing_images/w3vaildtor.png)

 # Products on all related pages
The image below is testing for the Products on all related pages only, javascript causing warnings.

![Testing on W3C Html](documentation/testing_images/w3vaildtor.png)

 #  Shopping Bag
The image below is testing for the bag page, javascript causing warnings.

![Testing on W3C Html](documentation/testing_images/w3vaildtor.png)

 # checkout
 The image below is testing for the checkout page, javascript causing warnings.
 The error is due to django crispy forms being used.

![Testing on W3C Html](documentation/testing_images/w3checkouterror.png)

# Product Management
 The image below is testing for the product management page ,javascript causing warnings. 

![Testing on W3C Html](documentation/testing_images/w3vaildtor.png)

# Profiles
 The image below is testing for the Score.html file. No errors or warnings are visible. 

![Testing on W3C Html](documentation/testing_images/w3vaildtor.png)

# CSS testing for all pages on base css
![Testing on W3C CSS](documentation/testing_images/csseshop.png)


# PEP8 Testing 
Testing on Pep8 shopping bag

![Testing on Pep8 shopping bag](documentation/testing_images/pep8/bagviewspep8.png)

Testing on Pep8 checkout_forms

![Testing on Pep8 checkout_forms](documentation/testing_images/pep8/checkout_forms.png)

Testing on Pep8 checkout models

![Testing on Pep8 checkout models](documentation/testing_images/pep8/checkoutmodels.png)

Testing on Pep8 checkout signals

![Testing on Pep8 checkout signals](documentation/testing_images/pep8/checkoutsignalspep8.png)

Testing on Pep8 checkout views

![Testing on Pep8 checkout views](documentation/testing_images/pep8/checkoutviewspep82.JPG)

Testing on Pep8 wishlist models

![Testing on Pep8 wishlist models](documentation/testing_images/pep8/wishlistmodelspep8.png)

Testing on Pep8 wishlist views

![Testing on Pep8 wishlist views](documentation/testing_images/wishlistviewspep8.png)

[Testing on Pep8 wishlist views

![Testing on Pep8 product views](documentation/testing_images/pep8/productviewspep8.png)

Testing on Pep8 product models

![Testing on Pep8 product models](documentation/testing_images/pep8/productmodelspep8.png)

Testing on Pep8 profile forms

![Testing on Pep8 profile forms](documentation/testing_images/pep8/profileformpep8.png)

Testing on Pep8 profile models

![Testing on Pep8 profile models](documentation/testing_images/pep8/profilemodelspep8.png)

Testing on Pep8 profile views

![Testing on Pep8 profile views](documentation/testing_images/pep8/profileviewspep8.png)


# Automated Testing
I would have liked to do more on this put due my limited understanding on this and very little coverage on this subject on the LMS i have only managed to incorporate 3 functioning test. I  have included images of the commits as proof of the test

![Automated testing](documentation/testing_images/eshopautomatedtest.png)
![Automated testing](documentation/testing_images/automated_test_commits.png)

# Build vs  Deployment 
| Test Build Vs Deployed Build                                         | Build Version                             | Deployed version       | Pass  | Errors   |
|----------------------------------------------------------------------|-------------------------------------------|------------------------|-------|----------|
| Nav Bar Functionality working correctly                              | No Issues                                 | Matches build version  | pass  | n/a      |
| Drop down menus                                                      | No Issues                                 | Matches build version  | pass  | n/a      |
| Search Bar functions                                                 | Working correctly                         | Matches build version  | pass  | n/a      |
| All links working on dropdown menus                                  | Working Correctly                         | Matches build version  | pass  | n/a      |
| Shop now button                                                      | Working Correctly                         | Matches build version  | pass  | n/a      |
| Product pages  card borders                                          | Appearing as intended                     | Matches build version  | pass  | n/a      |
| Free delivery banner text and background color                       | Appearing as intended                     | Matches build version  | pass  | n/a      |
| Image and text links taking you product details page                 | Appearing as intended                     | Matches build version  | pass  | n/a      |
| Edit and delete buttons appear on for admin only                     | Appearing as intended                     | Matches build version  | pass  | n/a      |
| Sort a list of items. By price, alphabetically, rating, and category | Appearing as intended                     | Matches build version  | pass  | n/a      |
| Order confirmation including what the user has bought                | Appearing as intended                     | Matches build version  | pass  | n/a      |
| User profile and personal information                                | Working Correctly                         | Matches build version  | pass  | n/a      |
| To be able to enter payment details to purchase items                | Working Correctly                         | Matches build version  | pass  | n/a      |
| Add products from an admin for on the website                        | Working Correctly                         | Matches build version  | pass  | n/a      |
| Quantity buttons resizing on different devices                       | Not working correctly on smaller devices  | Matches build version  | fail  | Resizing |
| Checkout pages and buttons working correctly                         | Working Correctly                         | Matches build version  | pass  | n/a      |
| Email Verification sent                                              | Working Correctly                         | Matches build version  | pass  | n/a      |
| Order history appearing on profiles pages                            | Working Correctly                         | Matches build version  | pass  | n/a      |
| Products appear on wish list once selected                           | Working Correctly                         | Matches build version  | pass  | n/a      |

### User Feedback vs Deployment  
| User Stories Vs deployed version                                | Achieved | Fail |
|-----------------------------------------------------------------|----------|------|
| All products have detailed description                          | Pass     | n/a  |
| The amount of products displayed on the page                    | Pass     | n/a  |
| Easy user interface                                             | Pass     | n/a  |
| Search bar                                                      | Pass     | n/a  |
| All available products in separate categories                   | Pass     | n/a  |
| Order conformation                                              | Pass     | n/a  |
| Secure site with card payment                                   | Pass     | n/a  |
| User profile with order history                                 | Pass     | n/a  |
| Login and registration features available                       | Pass     | n/a  |
| Password recovery                                               | Pass     | n/a  |
| Images and text have links to the product description           | Pass     | n/a  |
| Product form to edit and delete product inventory.              | Pass     | n/a  |
| Admin access to view all customers that use Eshop               | Pass     | n/a  |
| A feature to save personal information and delivery information | Pass     | n/a  |

### Responsiveness Testing 
| Responsiveness Test                             | Result                 | Pass |
|-------------------------------------------------|------------------------|------|
| All images resizes to fit the smaller cards     | Works correctly        | Pass |
| shopping bag buttons resize correctly           | Resizing issues        | Fail |
| Hamburger icon no colour                        | Fixed with in base css | Pass |
| Drop menu hamburger buttons on smaller devices  | Works correctly        | Pass |
| Image cards resize to 1 per  row                | Works correctly        | Pass |
| Search bar resize and still functions           | Works correctly        | Pass |
| Text resizes on smaller devices                 | Works correctly        | Pass |
| All buttons resize                              | Works correctly        | Pass |
| Quantity buttons and number bar resize          | Alignment issues       | Fail |
| Check forms resize to fit the page              | Works correctly        | Pass |
| Icon stack in rows of three on the nav bar      | Works correctly        | Pass |
| Mini shopping toast card resizes correctly      | Works correctly        | Pass |
| All toast messages resize to fit the devices    | Works correctly        | Pass |

# BUGS
  1. The only bugs i could find was on the checkout page, where text and the quantity input bars would not resize correctly 
  2. Javascript appearing in the source code even though i put them in separate js files. I have tried to fix as i wanted clean code through out my site.
  3. Toast javascript appearing on the base.html page I tired to put them in separate js file but was unable to get it to work.
  4. I know this isn`t technically a bug but due to the lack of automated testing on the LMS i was unable to put more test in this annoying as was trying to achieve a hire grade than a pass. 
  5. Testing on html validation for the checkout page throws up errors this due to Django crispy forms being implement in to framework. 

# Accessibility

![Testing on Lighthouse Reports Home](documentation/accessibility/eshopaccessibilityhome.png)

![Testing on Lighthouse Reports Profile](documentation/accessibility/eshopaccessibilityprofile.png)

![Testing on Lighthouse Reports Login](documentation/accessibility/eshopaccessibilitylogin.png)

![Testing on Lighthouse Reports Register](documentation/accessibility/eshopaccessibilityregister.png)

![Testing on Lighthouse Reports Products](documentation/accessibility/eshopaccessibilityproducts.png)

![Testing on Lighthouse Reports Product Management](documentation/accessibility/eshopaccessibilityproductmanagment.png)

![Testing on Lighthouse Reports Login Bag](documentation/accessibility/eshopaccessibilitybag.png)

![Testing on Lighthouse Reports Wishlist](documentation/accessibility/eshopaccessibilitywishlist.png)

![Testing on Lighthouse Reports Login Checkout](documentation/accessibility/eshopaccessibilitycheckout.png)

![Testing on Lighthouse Reports Order](documentation/accessibility/eshopaccessibilityorder.png)