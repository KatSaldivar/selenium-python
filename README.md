# Test Plan
The strategy for this test should encompass Functional behavior of this site, including CRUD behavior. It would also be good to test state changes, for example, when selecting items for the shopping cart and when they are purchased. 

# Sign in /sign out Functionality 
## Create an Account
1. Navigate to https://www.gouletpens.com
2. Click on the " Sign In / Sign Up" button on the top right
3. Fill out the form with a valid name, and email address, and password
4. Press submit and be redirected to the account page.
5. Look at the email inbox and verify the confirmation email has arrived. 

## Sign in
1. Navigate to https://www.gouletpens.com
2. Click on the " Sign In / Sign Up" button on the top right
3. Enter a valid email and password. 
4. Press submit and be redirected to the account page.

## Sign in form error validation  
1. Navigate to https://www.gouletpens.com
2. Click on the "Sign In / Sign Up" button on the top right
3. Enter an invalid email and password. 
4. Press submit and be redirected to the account page.

## Reset password
1. Navigate to https://www.gouletpens.com
2. Click on the "Sign In / Sign Up" button on the top right
3. Click the "forgot password" link

## Log out
Preconditions: The user is already logged into their account
1. Click on the "My account" button on the top right
2. Once the account page loads, select the "sign out" button on the bottom left
3. The user should be redirected to the site landing page. The "My account" button now is replaced with a "Sign In / Sign Up" button

## Reset password
1. Navigate to https://www.gouletpens.com
2. Click on the "Sign In / Sign Up" button on the top right
3. Click the "forgot password" link
4. Enter the email address associated with the account 
5. Press submit and verify the reset email has arrived in the inbox for the email address provided
6. Click the link from the email address and be redirected to a form for resetting a password
7. Enter a new password in the form and press submit.
8.  Press submit and be redirected to the account page.

# Wishlist Functionality
## Add an item to wishlist
Preconditions: The user is already logged into their account
1. Navigate to https://www.gouletpens.com
2. Click the "Shop Now" button for the featured pen
3. Click the "Add to wishlish" button
4. Click on the "My Wishlist" button on the top right
5. The pen that the user had selected to add to the wishlist is present in the list. 

## Remove an item from wishlist
Preconditions: The user is already logged into their account and already has items in their wishlist
1. Navigate to https://www.gouletpens.com
2. Click on the "My Wishlist" button on the top right
3. Click the Remove button below one of the items in the list
4. The pen is no longer present in the wishlist. 

## Remove all items from wishlist
Preconditions: The user is already logged into their account and already has items in their wishlist
1. Navigate to https://www.gouletpens.com
2. Click on the "My Wishlist" button on the top right
3. Click the "clear all" button 
4. The wishlist is now empty

## Share wishlist items
Preconditions: The user is already logged into their account and already has items in their wishlist
1. Navigate to https://www.gouletpens.com
2. Click on the "My Wishlist" button on the top right
3. Click the "share" button 
4. An alert should pop up with share options and a link to copy. 

# Review Functionality
## Add a Review to an item
Preconditions: The user is already logged into their account
1. Navigate to https://www.gouletpens.com
2. Select a pen to give a review
3. Scroll down and select the button to "Add a review"
4. Fill out the form and submit
5. Confirm the review was added. 

## Filter Reviews
Preconditions: The user is already logged into their account
1. Navigate to https://www.gouletpens.com
2. Select a pen that has a variety of ratings. such as this one: https://www.gouletpens.com/products/diamine-safari-40ml-bottled-ink?variant=11884619431979
3. Scroll down and filter the reviews by the ammount of stars. Select one star. 
4. The reviews listed should all match the same amount of starts that were selected in the filter.