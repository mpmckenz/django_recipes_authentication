<p align="center">
 <img src=try.png/>
</p>

# Django Recipebox: Authentication!

Django helps us out with a ton of stuff when it comes to starting a website, and authentication is no exception. By hooking into the backend for the admin panel and the helper functions that it gives us, we can roll our own authentication system fairly easily with only a few changes.

The goal of this assignment is to modify your recipe application to be able to protect those forms; we don't want just anyone adding recipes!

-   Add a user signup page where accounts can be created.
-   Add a login page so that people can sign in.
-   use the @login_required() decorator to lock your form views so that only logged in users can access them... but set them so that they require different permissions to access.
    -   The recipe add form can be accessed by any logged in user.
    -   The user add form can only be accessed by admins.
        -   (Hint: check the flag at `request.user.is_staff`)
-   On your home page, add a logout button that completes the logout process and dumps the user back on the homepage.

Extra credit, 5 points:

-   Make the recipe creation page change the Author attribute depending on whether or not the logged-in user is staff or not. If they are staff, list all available Authors as options. If they are not staff, make it so that they can only submit recipes as themselves.

[https://s3.us-east-2.amazonaws.com/videos.kenzie.academy/Software+Engineering+-+Python/2019-03-08+--+Auth+Overview.mp4](https://s3.us-east-2.amazonaws.com/videos.kenzie.academy/Software+Engineering+-+Python/2019-03-08+--+Auth+Overview.mp4)

---

### Rubric

1. Login portal at /login/
2. Logout link at /logout/
3. Clicking on either form when not logged in redirects to login page
4. After logging in, user is redirected back to form that was originally requested
5. Staff users can create users and create recipes
6. Non-staff users can create recipes but receive an error when they try to access the user creation page
7. Login url is stored in `settings.py`
8. Logout button functions as expected and redirects back to the homepage afterwards
