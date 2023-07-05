# Reader's angle
'Reader's angle' website project had been created as a final portfolio project for Code Institute full stack course! The project aims to provide an intuitive backend solution using Django Rest Framework.

At the core of this website, users can create posts dedicated to books, allowing them to express their thoughts, opinions, and recommendations for others to explore. Additionally, users have the opportunity to provide detailed reviews, offering valuable feedback on specific books and contributing to a vibrant literary community. By expressing their liking for posts and indicating their reading intentions (whether they have read a book or plan to read it), users can engage with books in a personalized and meaningful manner.

This project prioritizes comprehensive CRUD (Create, Read, Update, Delete) functionality for each model, granting users complete control over their interactions and experiences on the website.

## Links to front end repository and live site
If you would like to access the live site, click on the following link: [Reader's Angle live site](https://readersangle-frontend-2.herokuapp.com)

If you would like to access the front-end repository, click on the following link: [Reader's Angle front end repository](https://github.com/SilviaSaverino/readersangle-front-end)

# Models
Models are a fundamental aspect of building database-driven applications in Django. In Django, models represent the structure and behavior of the data that is stored in the database. They define the tables, fields, relationships, and constraints that make up the data schema.

![screenshot of the project schema](/repo_images/schema.png)

## Profile Model:
![screenshot of profile model](repo_images/profile_model.png)

The Profile model represents user profiles and contains information such as the owner, creation and update timestamps, name, bio, and image.

Fields:
- owner: One-to-One relationship field linking to the User model, representing the owner of the profile.
- created_at: DateTimeField automatically set to the current date and time when the profile is created.
- updated_at: DateTimeField automatically updated to the current date and time whenever the profile is modified.
- name: CharField with a maximum length of 255 characters, allowing for an optional name for the profile.
- bio: TextField allowing for an optional bio or description for the profile.
- image: ImageField specifying the location where profile images are uploaded. It uses the 'images/' directory as the upload      destination and has a default image specified as '../default_profile_xyw4hp'.

The Meta class within the Profile model specifies the ordering of profile instances based on their creation timestamps. Profiles are ordered in descending order by created_at.

The model includes a __str__ method that returns a string representation of the profile, indicating the owner's username.

A create_profile function is defined as a signal receiver and connected to the post_save signal of the User model. This function automatically creates a profile for a newly created user.

## Post model:
![screenshot of post model](/repo_images/post_model.png)

The Post model represents posts related to owners/users. Each post contains information such as the owner, title, author, genre, content, creation and update timestamps, image, image filter, and genre filter.

Fields:
- owner: ForeignKey field linking to the User model, representing the owner of the post.
- title: CharField with a maximum length of 255 characters, allowing for an optional title for the post.
- author: CharField with a maximum length of 255 characters, allowing for an optional author for the post.
- genre: CharField with a maximum length of 255 characters, allowing for an optional genre for the post.
- content: TextField allowing for optional content or text associated with the post.
- created_at: DateTimeField automatically set to the current date and time when the post is created.
- updated_at: DateTimeField automatically updated to the current date and time whenever the post is modified.
- image: ImageField specifying the location where post images are uploaded. It uses the 'images/' directory as the upload destination and has a default image specified as '../default_book_w68xtp'.
- image_filter: CharField with a maximum length of 30 characters, providing choices for different image filters that can be applied to the post image. The default filter is set to 'normal'.
- genre_filter: CharField with a maximum length of 30 characters, providing choices for different genre filters that can be applied to the post. The default filter is set to 'normal'.

The Meta class within the Post model specifies the ordering of post instances based on their creation timestamps. Posts are ordered in descending order by created_at.

The model includes a __str__ method that returns a string representation of the post, displaying the post's ID and title.

## Post Follower Model:
![screenshot of postfollowers model](/repo_images/postfollowers_model.png)

The PostFollower model represents the followers of posts in the application. It establishes a connection between the 'owner' (user) and the 'followed_post'. The model includes a timestamp for when the follow action was created.

Fields:
- owner: This field is a foreign key referencing the User model from Django's built-in authentication system. It establishes a relationship between the PostFollower model and the user who is following the post. When a user is deleted, all associated post followers will be removed as well.
- followed_post: This field is a foreign key referencing the Post model from the 'posts' application. It represents the post being followed. When a post is deleted, all associated post followers will be removed as well.
- created_at: This field is a DateTimeField with the auto_now_add attribute set to True. It automatically records the date and time when the follow action is created.

The PostFollower model includes the following Meta options:
- unique_together: The unique_together option ensures that a user cannot follow the same post multiple times. It enforces uniqueness by specifying that the combination of 'owner' and 'followed_post' fields must be unique.

Methods:
- str(): This method returns a string representation of the PostFollower object. It displays the owner's username and the post ID being followed in the format: "[owner's username] follows post [post ID]".

## Post Status Model
![screenshot of poststatus model](/repo_images/poststatus_model.png)

The PostStatus model represents the status of a post for a specific user. It allows users to indicate whether they have read a post or intend to read it in the future.

Fields:
- owner: This field is a foreign key referencing the User model from Django's built-in authentication system. It establishes a relationship between the PostStatus model and the user who has a status for a post. When a user is deleted, all associated post statuses will be removed as well.
- post: This field is a foreign key referencing the Post model from the 'posts' application. It represents the post for which the status is being recorded. When a post is deleted, all associated post statuses will be removed as well.
- profile: This field is a foreign key referencing the Profile model from the 'profiles' application. It represents the profile associated with the user who has a status for a post. When a profile is deleted, all associated post statuses will be removed as well. The default value is set to 0.
- status: This field is a CharField with a maximum length of 15 characters. It allows users to choose a status for the post from predefined choices. The available choices are 'Read' and 'Will read'. Users can indicate whether they have read the book the post is about or plan to read it in the future.

Methods:
- str(): This method returns a string representation of the PostStatus object. It displays the owner and the post in the format: "[owner] [post]".

## Like Model:
![screenshot of like model](/repo_images/like_model.png)

The Like model represents a user's liking activity in relation to a specific post. It establishes a connection between the 'owner' (user) and the 'post' being liked. The model includes a timestamp for when the like was created.

Fields:
- owner: This field is a foreign key referencing the User model from Django's built-in authentication system. It establishes a relationship between the Like model and the user who performed the like. When a user is deleted, all associated likes will be removed as well.
- post: This field is a foreign key referencing the Post model from the 'posts' application. It represents the post that was liked. When a post is deleted, all associated likes will be removed as well.
- created_at: This field is a DateTimeField with the auto_now_add attribute set to True. It automatically records the date and time when the like is created.

The Like model includes the following Meta options:
- ordering: The ordering option specifies that the likes should be ordered in descending order based on the 'created_at' field.   This ensures that the most recent likes appear first in queries.
- unique_together: The unique_together option ensures that a user cannot like the same post twice. It enforces uniqueness by specifying that the combination of 'owner' and 'post' fields must be unique.

Methods:
- str(): This method returns a string representation of the Like object. It displays the owner and the post in the format: "[owner] [post]".

## Review Model: 
![screenshot of review model](/repo_images/reviews_model.png)

The Review model represents reviews related to users and posts. Each review contains information such as the owner, post, creation and update timestamps, and content.

Fields:
- owner: ForeignKey field linking to the User model, representing the owner of the review.
- post: ForeignKey field linking to the Post model, representing the post associated with the review.
- created_at: DateTimeField automatically set to the current date and time when the review is created.
- updated_at: DateTimeField automatically updated to the current date and time whenever the review is modified.
- content: TextField representing the content or text of the review.

The Meta class within the Review model specifies the ordering of review instances based on their creation timestamps. Reviews are ordered in descending order by created_at.

The model includes a __str__ method that returns a string representation of the review, displaying the review's content.

## ReviewLikes Model:
![screenshot of reviewlikes model](/repo_images/reviewlikes_model.png)

The ReviewLike model represents the likes for reviews in the application. It establishes a connection between the 'owner' (user) and the 'review' being liked. The model includes a timestamp for when the like was created.

Fields:
- owner: This field is a foreign key referencing the User model from Django's built-in authentication system. It establishes a relationship between the ReviewLike model and the user who performed the like. When a user is deleted, all associated review likes will be removed as well.
- review: This field is a foreign key referencing the Review model from the 'reviews' application. It represents the review that was liked. When a review is deleted, all associated review likes will be removed as well.
- created_at: This field is a DateTimeField with the auto_now_add attribute set to True. It automatically records the date and time when the like is created.

The ReviewLike model includes the following Meta options:
- ordering: The ordering option specifies that the review likes should be ordered in descending order based on the 'created_at' field. This ensures that the most recent likes appear first in queries.
- unique_together: The unique_together option ensures that a user cannot like the same review twice. It enforces uniqueness by specifying that the combination of 'owner' and 'review' fields must be unique.

Methods:
- str(): This method returns a string representation of the ReviewLike object. It displays the owner who liked the review and the review itself in the format: "[owner] liked the review [review]".

# Serializers
Serializers play a crucial role in Django when it comes to handling data serialization and deserialization in web APIs. In Django, serializers are responsible for converting complex data types, such as model instances, into formats that can be easily rendered into JSON, XML, or other content types for client consumption.

In this project, serializers have been implemented to handle the conversion of various models and data structures into appropriate formats for API responses. Each serializer defines the fields and their corresponding mappings to the data models, allowing for seamless data transformation and transmission.

## Profile Serializer
The ProfileSerializer is responsible for serializing and deserializing data related to the Profile model. It defines how the Profile instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the profile owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the profile.
- posts_count: A read-only field that represents the count of posts associated with the profile.
- reviews_count: A read-only field that represents the count of reviews associated with the profile.
- read_posts_count: A custom field that retrieves the count of posts marked as "Read" for the profile.
- will_read_posts_count: A custom field that retrieves the count of posts marked as "Will read" for the profile.

Methods
- get_is_owner(obj): This method is a SerializerMethodField that checks whether the authenticated user is the owner of the profile (obj).
- get_read_posts_count(obj): This method is a SerializerMethodField that retrieves the count of posts marked as "Read" for the profile (obj).
- get_will_read_posts_count(obj): This method is a SerializerMethodField that retrieves the count of posts marked as "Will read" for the profile (obj).

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Profile model. The specified fields include: id, owner, created_at, updated_at, name, bio, image, is_owner, posts_count, reviews_count, read_posts_count, and will_read_posts_count.

## Post Serializer
The PostSerializer is responsible for serializing and deserializing data related to the Post model. It defines how the Post instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the post owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the post.
- profile_id: A read-only field that represents the ID of the owner's profile.
- profile_image: A read-only field that represents the URL of the owner's profile image.
- following_id: A custom field that retrieves the ID of the post follower, if the authenticated user follows the post.
- like_id: A custom field that retrieves the ID of the like associated with the post, if the authenticated user has liked the post.
- likes_count: A read-only field that represents the count of likes associated with the post.
- review_count: A read-only field that represents the count of reviews associated with the post.
- followed_count: A read-only field that represents the count of followers for the post.
- post_status: A custom field that retrieves the status of the post for the authenticated user.

Methods
- validate_image(value): This method validates the size and dimensions of the image field. It checks if the image size is larger than 2MB and if the height and width exceed 4096 pixels.
- get_is_owner(obj): This method is a SerializerMethodField that checks whether the authenticated user is the owner of the post (obj).
- get_following_id(obj): This method is a SerializerMethodField that retrieves the ID of the post follower if the authenticated user follows the post.
- get_like_id(obj): This method is a SerializerMethodField that retrieves the ID of the like associated with the post if the authenticated user has liked the post.
- get_post_status(obj): This method is a SerializerMethodField that retrieves the status of the post for the authenticated user.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Post model. The specified fields include: id, owner, profile_id, profile_image, created_at, updated_at, title, author, content, image, is_owner, genre_filter, image_filter, following_id, like_id, likes_count, review_count, followed_count, and post_status.

## PostFollower Serializer:
The PostFollowerSerializer is responsible for serializing and deserializing data related to the PostFollower model. It defines how PostFollower instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the user who is following the post.
- followed_post: A field that allows selection of the followed post by its ID from the queryset of all posts.
- followed_post_title: A read-only field that represents the title of the followed post.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the PostFollower model. The specified fields include: id, owner, created_at, followed_post, followed_post_title

Methods:
- create(): This method overrides the default create() method of the serializer. It attempts to create a new PostFollower instance with the provided validated data. If an IntegrityError occurs, indicating a possible duplicate entry where a user is already following the post, it raises a serializers.ValidationError with the detail message "Post already followed by user. Possible duplicate."
- get_followed_post_title(obj): This method is a SerializerMethodField that retrieves and returns the title of the followed post for a given PostFollower object (obj).

## PostStatus Serializer:
The PostStatusSerializer is responsible for serializing and deserializing data related to the PostStatus model. It defines how PostStatus instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the owner of the post status.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the PostStatus model. The specified fields include: id, post, owner, status

Methods:
- create(validated_data): This method overrides the default create() method of the serializer. It creates a new instance of the serializer's model using the provided validated data. 
If a duplicate status for the post and user is detected, the existing instance is updated with the new status instead of creating a new one. It first checks if an existing instance with the same post and owner exists. 
If found, it updates the status of the existing instance and saves it. 
If no existing instance is found, it attempts to create a new instance with the validated data. 
If an IntegrityError occurs during creation, it raises a serializers.ValidationError with the detail message "An error occurred while creating the post status."

## Like Serializer:
The LikeSerializer is responsible for serializing and deserializing data related to the Like model. It defines how Like instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the owner of the like.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Like model. The specified fields include: id, post, owner, created_at

Methods:
- create(validated_data): This method overrides the default create() method of the serializer. It creates a new instance of the serializer's model using the provided validated data. 
If a duplicate like for the post and user is detected, a serializers.ValidationError is raised with the detail message "Post already liked by the user. Possible duplicate." The duplication is checked by catching the IntegrityError exception.

## Review Serializer
The ReviewSerializer is responsible for serializing and deserializing data related to the Review model. It defines how the Review instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the review owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the review.
- profile_id: A read-only field that represents the ID of the owner's profile.
- profile_image: A read-only field that represents the URL of the owner's profile image.
- reviewlike_id: A custom field that retrieves the ID of the like associated with the review if the authenticated user has liked the review.
- reviewlikes_count: A read-only field that represents the count of likes associated with the review.
The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Review model. The specified fields include: id, owner, post, profile_id, profile_image, created_at, updated_at, content, and is_owner.

Methods
- get_is_owner(obj): This method is a SerializerMethodField that checks whether the authenticated user is the owner of the review (obj).
- get_reviewlike_id(obj): This method is a SerializerMethodField that retrieves the ID of the like associated with the review if the authenticated user has liked the review.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Review model. The specified fields include: id, owner, post, profile_id, profile_image, created_at, updated_at, content, is_owner, reviewlike_id, and reviewlikes_count.

### Review Detail Serializer
The ReviewDetailSerializer is a subclass of ReviewSerializer and is used specifically for the detail view of a review. It adds an additional field:
- post: A read-only field that represents the ID of the associated post.

## ReviewLike Serializer:
The ReviewLikeSerializer is responsible for serializing and deserializing data related to the ReviewLike model. It defines how ReviewLike instances are represented in JSON format.

The serializer includes the following fields:
-owner: A read-only field that represents the username of the owner of the review like.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the ReviewLike model. The specified fields include: id, review, owner, created_at

Methods:
- create(validated_data): This method overrides the default create() method of the serializer. It creates a new instance of the serializer's model using the provided validated data. 
If a duplicate like for the review and user is detected, a serializers.ValidationError is raised with the detail message "Review already liked by the user. Possible duplicate." The duplication is checked by catching the IntegrityError exception.

# API Views 
API views are an essential component of building web applications and services that expose data and functionality through an API (Application Programming Interface). In the context of Django, API views are used to define how data is accessed, manipulated, and presented in a web API.

In this project, the API views have been designed and implemented to handle specific resources such as posts, reviews, likes, etc. Each API view has its own set of actions and permissions defined to meet the specific requirements of the application.

## PostList API View:
The PostList API view allows for listing all posts or creating a new post if the user is logged in. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /posts/ endpoint retrieves a list of all posts. If the user is authenticated, they can also use a POST request to create a new post. The post data is serialized using the PostSerializer class.

To ensure that only authenticated users can create posts, the IsAuthenticatedOrReadOnly permission class is used. This allows read access to anyone (even unauthenticated users) but only allows write access to authenticated users.

The perform_create method is overridden to associate the created post with the logged-in user. By saving the owner field of the post with the current user, the post is automatically linked to the user who created it.

## PostDetail API View:
The PostDetail API view is responsible for retrieving, updating, and deleting a specific post. It is implemented as a RetrieveUpdateDestroyAPIView from the Django generics module.

A GET request to the /posts/<int:pk>/ endpoint retrieves a specific post identified by its post_id. If the user is the owner of the post, they can also perform update and delete operations on the post using the appropriate request methods.

The PostSerializer class is used to serialize and deserialize the post data, ensuring consistent representation of the post in JSON format.

To restrict access and ensure that only the owner of the post can modify or delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the post.

By utilizing the power of Django's generics module and the provided view classes, the PostList and PostDetail views offer a straightforward and efficient way to handle listing, creation, retrieval, updating, and deletion of posts.

## PostFollowerList API View:
The PostFollowerList API view is responsible for listing all post followers and creating a new post follower (i.e., following a post) if the user is logged in. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /post-followers/ endpoint retrieves a list of all post followers. If the user is authenticated, they can use a POST request to create a new post follower, which means they will start following a post. The post follower data is serialized using the PostFollowerSerializer class.

To ensure that only authenticated users can create post followers, the IsAuthenticatedOrReadOnly permission class is used. This permission class allows read access to anyone (even unauthenticated users) but only allows write access to authenticated users.

The perform_create method is overridden to associate the created post follower with the logged-in user. By saving the owner field of the post follower with the current user, the post follower is automatically linked to the user who created it.

## PostFollowerDetail API View:
The PostFollowerDetail API view is responsible for retrieving and deleting a specific post follower. It is implemented as a RetrieveDestroyAPIView from the Django generics module.

A GET request to the endpoint 'post_followers/<int:pk>/' retrieves a specific post follower identified by its post_follower_id. The post follower data is serialized using the PostFollowerSerializer class.

A DELETE request to the same endpoint deletes the post follower, which means the user will stop following the post. However, there is no update view for post followers, as they can only be followed or unfollowed.

To restrict access and ensure that only the owner of the post follower can delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the post follower.

## PostStatusList API View:
The PostStatusList API view is responsible for listing all PostStatus instances and creating new PostStatus instances. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /post-status/ endpoint retrieves a list of all PostStatus instances. If the user is authenticated, they can use a POST request to create a new PostStatus instance. The PostStatus data is serialized using the PostStatusSerializer class.

To control access, the IsAuthenticatedOrReadOnly permission class is used. This permission class allows read access to anyone (even unauthenticated users) but only allows write access to authenticated users.

The perform_create method is overridden to associate the created PostStatus instance with the logged-in user. By saving the owner field of the PostStatus instance with the current user, the instance is automatically linked to the user who created it.

## PostStatusDetail API View:
The PostStatusDetail API view is responsible for retrieving, updating, and deleting a specific PostStatus instance. It is implemented as a RetrieveUpdateDestroyAPIView from the Django generics module.

A GET request to the /post-status/<int:pk>/ endpoint retrieves a specific PostStatus instance identified by its post_status_id. The PostStatus data is serialized using the PostStatusSerializer class.

A PUT request to the same endpoint updates the PostStatus instance with the provided data. A DELETE request deletes the PostStatus instance.

To control access and ensure that only the owner of the PostStatus instance can modify or delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the PostStatus instance.

## LikeList API View:

The LikeList API view is responsible for listing all likes and creating a new like if the user is logged in. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /likes/ endpoint retrieves a list of all likes. If the user is authenticated, they can also use a POST request to create a new like. The like data is serialized using the LikeSerializer class.

To ensure that only authenticated users can create likes, the IsAuthenticatedOrReadOnly permission class is used. This permission class allows read access to anyone (including unauthenticated users) but only allows write access to authenticated users.

The perform_create method is overridden to associate the created like with the logged-in user. By saving the owner field of the like with the current user, the like is automatically linked to the user who created it.

## LikeDetail API View:

The LikeDetail API view is responsible for retrieving and deleting a specific like. It is implemented as a RetrieveDestroyAPIView from the Django generics module.

A GET request to the /likes/int:pk/ endpoint retrieves a specific like identified by its like_id. If the user is the owner of the like, they can also perform delete operation on the like using the appropriate request method.

The LikeSerializer class is used to serialize and deserialize the like data, ensuring consistent representation of the like in JSON format.

To restrict access and ensure that only the owner of the like can delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the like.

## ReviewList API View:
The ReviewList API view provides functionality for listing all reviews and creating a new review if the user is logged in. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /reviews/ endpoint retrieves a list of all reviews. If the user is authenticated, they can also use a POST request to create a new review. The review data is serialized using the ReviewSerializer class.

To ensure that only authenticated users can create reviews, the IsAuthenticatedOrReadOnly permission class is used. This allows read access to anyone (including unauthenticated users), but only allows write access to authenticated users.

The perform_create method is overridden to associate the created review with the logged-in user. By saving the owner field of the review with the current user, the review is automatically linked to the user who created it.

## ReviewDetail API View:

The ReviewDetail API view is responsible for retrieving, updating, and deleting a specific review. It is implemented as a RetrieveUpdateDestroyAPIView from the Django generics module.

A GET request to the /reviews/int:pk/ endpoint retrieves a specific review identified by its review_id. If the user is the owner of the review, they can also perform update and delete operations on the review using the appropriate request methods.

The ReviewDetailSerializer class is used to serialize and deserialize the review data, ensuring consistent representation of the review in JSON format.

To restrict access and ensure that only the owner of the review can modify or delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the review.

## ReviewLikeList API View:

The ReviewLikeList API view is designed for listing all review likes and creating a new review like if the user is logged in. It is implemented as a ListCreateAPIView from the Django generics module.

A GET request to the /review-likes/ endpoint retrieves a list of all review likes. If the user is authenticated, they can also use a POST request to create a new review like. The review like data is serialized using the ReviewLikeSerializer class.

To ensure that only authenticated users can create review likes, the IsAuthenticatedOrReadOnly permission class is used. This permission class allows read access to anyone (including unauthenticated users) but only allows write access to authenticated users.

The perform_create method is overridden to associate the created review like with the logged-in user. By saving the owner field of the review like with the current user, the review like is automatically linked to the user who created it.

## ReviewLikeDetail API View:

The ReviewLikeDetail API view is responsible for retrieving and deleting a specific review like. It is implemented as a RetrieveDestroyAPIView from the Django generics module.

A GET request to the /review-likes/int:pk/ endpoint retrieves a specific review like identified by its like_id. If the user is the owner of the review like, they can also perform delete operation on the review like using the appropriate request method.

The ReviewLikeSerializer class is used to serialize and deserialize the review like data, ensuring consistent representation of the review like in JSON format.

To restrict access and ensure that only the owner of the review like can delete it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the review like.

## ProfileList API View:

The ProfileList API view allows for listing all profiles. Profile creation is handled by Django signals, which automatically creates a profile when a new user is registered. It is implemented as a ListAPIView from the Django REST Framework generics module.

A GET request to the /profiles/ endpoint retrieves a list of all profiles. The profiles are ordered by their creation date in descending order (-created_at). The profile data is serialized using the ProfileSerializer class.

The view also supports ordering of the profiles based on various fields such as posts_count, reviews_count, read_posts_count, and will_read_posts_count. The ordering can be controlled using the ordering query parameter in the request URL.

## ProfileDetail API View:

The ProfileDetail API view is responsible for retrieving and updating a specific profile if the current user is the owner. It is implemented as a RetrieveUpdateAPIView from the Django REST Framework generics module.

A GET request to the /profiles/int:pk/ endpoint retrieves a specific profile identified by its profile ID. If the user is the owner of the profile, they can also perform update operations on the profile using the appropriate request methods.

The ProfileSerializer class is used to serialize and deserialize the profile data, ensuring consistent representation of the profile in JSON format.

To restrict access and ensure that only the owner of the profile can modify it, the IsOwnerOrReadOnly permission class is used. This permission class allows read access to anyone but only allows write access to the owner of the profile.

# Manual testing:

| Feature          | Action                                                          | Expected Result                                     | Actual Result |
| ---------------- | --------------------------------------------------------------- | --------------------------------------------------- | ------------- |
|Profile:          |
| List Profiles    | Perform GET request to /api/profiles/                           | Retrieve a list of all user profiles                | Passed!       |
| Retrieve Profile | Perform GET request to /api/profiles/:id/                       | Retrieve a specific profile by its ID               | Passed!       |
| Update Profile   | Perform PUT request to /api/profiles/:id/ with updated data     | Update a specific profile by its ID                 | Passed!       |
||
| List Posts       | Perform GET request to /api/posts/                              | Retrieve a list of all posts                        | Passed!       |
| Create Post      | Perform POST request to /api/posts/ with title and content      | Create a new post and return the created post       | Passed!       |
| Update Post      | Perform PUT request to /api/posts/:id/ with updated data        | Update a specific post by its ID                    | Passed!       |
| Delete Post      | Perform DELETE request to /api/posts/:id/                       | Delete a specific post by its ID                    | Passed!       |
||
|Poststatus :      |
| List Poststatus     | Perform GET request to /api/poststatus/                        | Retrieve a list of post status (read/will read)   | Passed!       |
| Create Poststatus   | Perform POST request to /api/postsstatus/ with post ID         | Create a new poststatus for a post and return it  | Passed!       |
| Retrieve Poststatus | Perform GET request to /api/postsstatus/:id/                   | Retrieve a specific postsstatus by its ID         | Passed!       |
| Update Poststatus   | Perform PUT request to /api/postsstatus/:id/ with updated data | Update a specific poststatus by its ID            | Passed!       |
| Delete Poststatus   | Perform DELETE request to /api/poststatus/:id/                 | Delete a specific poststatus by its ID            | Passed!       |
||
|Postfollowers :   |
| List Post_followers   | Perform GET request to /api/post_followers/                | Retrieve a list of all posts                        | Passed!       |
| Create Post_followers | Perform POST request to /api/post_followers/ with post ID  | Create a new post and return the created post       | Passed!       |
| Delete Post_followers | Perform DELETE request to /api/post_followers/:id/         | Delete a specific post by its ID                    | Passed!       |
||
|Likes :           |
| List Likes       | Perform GET request to /api/likes/                              | Retrieve a list of all user likes                   | Passed!       |
| Create Likes     | Perform POST request to /api/likes/ with post ID                | Create a new like and return the created one        | Passed!       |
| Retrieve Likes   | Perform GET request to /api/likes/:id/                          | Retrieve a specific like by its ID                  | Passed!       |
| Delete Likes     | Perform DELETE request to /api/likes/:id/                       | Delete a specific like by its ID                    | Passed!       |
||
|Reviews :         |
| List Reviews     | Perform GET request to /api/reviews/                            | List all reviews                                    | Passed!       |
| Create Reviews   | Perform POST request to /api/reviews/ with content and post ID  | Create a new review and return the created one      | Passed!       |
| Retrieve Reviews | Perform GET request to /api/reviews/:id/                        | Retrieve a specific reviews by its ID               | Passed!       |
| Update Reviews   | Perform PUT request to /api/reviews/:id/ with updated data      | Update a specific reviews by its ID                 | Passed!       |
| Delete Reviews   | Perform DELETE request to /api/reviews/:id/                     | Delete a specific reviews by its ID                 | Passed!       |
||
|Reviewlikes :         |
| List Reviewlikes     | Perform GET request to /api/reviewslikes/                   | List all reviewlikes                                | Passed!       |
| Create Reviewlikes   | Perform POST request to /api/reviewslikes/                  | Create a new reviewlike and return the created one  | Passed!       |
| Retrieve Reviewlikes | Perform GET request to /api/reviewslikes/:id/               | Retrieve a specific reviewlike by its ID            | Passed!       |
| Delete Reviewlikes   | Perform DELETE request to /api/reviewslikes/:id/            | Delete a specific reviewlike by its ID              | Passed!       |


# Bugs and Debugging:
## Cloudinary issues with default images:
I've encountered an issue with cloudinary default profile image. It simply didn't load as expected and upon investigation this is what it was shown:
![screenshot of cloudinary profile image bug](repo_images/cloudinary_bug.png)

After realizing that the issue wasn't with my models but with some other images in Cloudinary, I took the following steps to fix it:
- I deleted any duplicate images from my Cloudinary storage.
- I uploaded new default images for posts and profiles to the Cloudinary media library.
- I edited the default image fields in both models to match the names of the new images.
- To make sure everything was up to date, I cleared the cache.
- In the admin panel, I created a new profile and a new post to see if the images were now displaying properly.

After completing these steps, I clicked on the posts and profile default images in their respective lists, and I was relieved to see that they were now displaying correctly.

![screenshot of default post image](/repo_images/bug_postimage.png)

![screenshot of default profile image](/repo_images/but_profileimage.png)

## TypeError in postFollower:
### Snippet of a shown error:

" Got a `TypeError` when calling `PostFollower.objects.create()`. This may be because you have a writable field on the serializer class that is not a valid argument to `PostFollower.objects.create()`. You may need to make the field read-only, or override the PostFollowerSerializer.create() method to handle this correctly. "
--------------------------------------------------------------------------------------------------------------------------------

During development, an issue was encountered where users were unable to follow posts due to some errors in my model and lately a TypeError in the code. The error occurred because the serializer was trying to pass an unexpected keyword argument to the PostFollower.objects.create() method. The problem was resolved by updating the model and its serializer's create() method to handle the creation of the PostFollower object correctly.

# Deployment:

## Deploying to Heroku
Follow these steps to deploy your application to Heroku:

### Create a PostgreSQL Database on ElephantSQL
- Go to ElephantSQL and log in or create a new account.
- Access the Dashboard and click "Create New Instance".
- Provide a name for the database and select the Tiny Turtle plan and region.
- Click the "Review" button and then "Create Instance".
- Copy the database URL for later use.

### Create an App on Heroku
- Visit Heroku and log in or create a new account.
- Click on "Create new app".
- Give your app a name and click "Create app".
- Open the "Settings" tab and add a Config Var for "DATABASE_URL". Paste the URL of the PostgreSQL database created on ElephantSQL.

### Set up the GitPod Workspace

Before deploying to Heroku, make the following changes in the GitPod workspace:

-Install the necessary packages for Heroku to connect to external databases:

    $ pip install dj_database_url==0.5.0 psycopg2

-Import dj_database_url in settings.py:

    import os
    import dj_database_url

-Update the DATABASES section in settings.py to distinguish between the development and production databases:

    if 'DEV' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }

-Add the following line to env.py to link to the PostgreSQL database URL:

    os.environ.setdefault("DATABASE_URL", "PostgreSQL URL")

-Test the Database Connection

-Comment out the DEV environment variable in env.py:

    os.environ['CLOUDINARY_URL'] = "cloudinary://..."
    os.environ['SECRET_KEY'] = "..."
    (COMMENTEDOUT FOR NOW->)os.environ['DEV'] = '1'
    os.environ['DATABASE_URL'] = "postgres://..."

-Add a print("connected") statement to the else clause in the DATABASES section of settings.py to verify the connection.

-Perform a dry-run migration to confirm the connection to the external database. If it works, you can remove the print statement:

    manage.py makemigrations --dry-run

-Migrate the database:

    manage.py migrate

-Create a superuser:

    manage.py createsuperuser

### GitPod Workspace Setup

-Install gunicorn and update requirements.txt:

    $ pip install gunicorn django-cors-headers
    $ pip freeze --local > requirements.txt

-Create a Procfile and add the following lines:

    release: python manage.py makemigrations && python manage.py migrate
    web: gunicorn '<your_app_name>.wsgi'

-Add the allowed hosts to settings.py:

    ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']

-Add corsheaders to INSTALLED_APPS in settings.py:

    INSTALLED_APPS = [
        ...
        'dj_rest_auth.registration',
        'corsheaders',
        ...
    ]

-Add the corsheaders middleware at the top of the MIDDLEWARE list in settings.py:

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]

-Set the CORS_ALLOWED_ORIGINS or CORS_ALLOWED_ORIGIN_REGEXES based on the environment variables in settings.py:

    if 'CLIENT_ORIGIN' in os.environ:
        CORS_ALLOWED_ORIGINS = [
            os.environ.get('CLIENT_ORIGIN')
        ]
    else:
        CORS_ALLOWED_ORIGIN_REGEXES = [
            r"^https://.*\.gitpod\.io$",
        ]

-Enable sending cookies in cross-origin requests by adding the following code in settings.py:

    CORS_ALLOW_CREDENTIALS = True

-Set the JWT_AUTH_SAMESITE attribute to 'None' to allow cross-platform deployment in settings.py:

    JWT_AUTH_SAMESITE = 'None'

-Set the SECRET_KEY in settings.py to retrieve it from the environment variable:

    SECRET_KEY = os.getenv('SECRET_KEY')

-Update the value of the SECRET_KEY environment variable in env.py with a new random value:

    os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")

-Set the DEBUG value to True only if the DEV environment variable exists in env.py:

    DEBUG = 'DEV' in os.environ

-Uncomment the DEV environment variable in env.py:

    import os

    os.environ['CLOUDINARY_URL'] = "cloudinary://..."
    os.environ['SECRET_KEY'] = "..."
    os.environ['DEV'] = '1'
    os.environ['DATABASE_URL'] = "postgres://..."

-Ensure that the project's requirements.txt file is up to date. In the GitPod terminal, enter the following command:

    $ pip freeze --local > requirements.txt

## Heroku Deployment

-Add the SECRET_KEY and CLOUDINARY_URL as Config Vars in Heroku. The SECRET_KEY is a randomly generated string, and the CLOUDINARY_URL is copied from settings.py.

-To fix the dj-rest-auth logout bug, create a custom logout view that sends an expired token to force logout. You can copy the code from this repository and update the URLs in this file.

-Modify the ALLOWED_HOSTS in settings.py to make the Heroku host an environment variable to prevent multiple instances:

    ALLOWED_HOSTS = [
        os.environ.get('ALLOWED_HOST'),
        'localhost',
    ]

-Add the Heroku app name as an additional config var named ALLOWED_HOST in Heroku.

-Add CLIENT_ORIGIN_DEV to allow development of the front-end with GitPod. Replace the else statement in the if 'CLIENT_ORIGIN...' block with the following code:

    if 'CLIENT_ORIGIN_DEV' in os.environ:
        extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
        CORS_ALLOWED_ORIGIN_REGEXES = [
            rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
        ]

-Commit and push the changes to GitHub.

-In Heroku, go to the "Deploy" tab.

-Select "Connect to GitHub".

-Choose your project repository.

-Click on "Connect" to establish the connection.

-Use "Deploy Branch" from the Manual Deploy section.

-Select the main branch and click "Deploy".

# Technologies and Frameworks Utilized:

### Programming Languages:
- Python

### Web Frameworks:
- Django: A high-level Python web framework employed for developing the project.
- djangorestframework: A toolkit utilized for constructing web APIs with Django.

### External Python Packages:
- asgiref: ASGI (Asynchronous Server Gateway Interface) framework.
- cloudinary: Integration with Cloudinary.
- dj-database-url: Enables the utilization of the 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
- dj-rest-auth: API endpoints for handling authentication in Django Rest Framework.
- Django: High-level Python web framework.
- django-allauth: A set of Django applications used for account registration, management, and authentication.
- django-cloudinary-storage: Integration with Cloudinary.
- django-cors-headers: A Django app that adds CORS headers to responses.
- django-filter: An application that allows dynamic QuerySet filtering from URL parameters.
- djangorestframework: Toolkit for building web APIs.
- djangorestframework-simplejwt: JSON Web Token authentication backend for the Django REST Framework.
- gunicorn: Python WSGI HTTP server.
- oauthlib: OAuth library for Python.
- Pillow: Fork of PIL, the Python Imaging Library, providing image processing capabilities.
- psycopg2: Python PostgreSQL database adapter.
- PyJWT: JSON Web Token implementation for Python.
- python3-openid: OpenID authentication for Python.
- pytz: World timezone definitions for Python.
- requests-oauthlib: OAuth library for Python requests.
- sqlparse: Library for parsing SQL statements in Python.
- python-dotenv: Sets key-value pairs from the .env file as environmental variables.

# Credits
To complete this project, I relied on various sources of information, including articles found online. I've mainly referred to module of CodeInstitute and took references from other alumnis projects.

# Acknowledgements
I would like to thank my mentor Spencer for his support and for taking the time to review this project.
I am thankful for my dear friend Francesco for being a constant source of support, and for my family members Martina and Cosimo for their love and encouragement. I would also like to acknowledge the creators and contributors of the online resources mentioned in the Credits section for providing valuable guidance and insights.
