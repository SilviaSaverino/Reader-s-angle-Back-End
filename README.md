# Reader's angle - 5th portfolio project for CodeInstitute full stack course.

## Bugs and Debugging:

I've encountered an issue with cloudinary default profile image. It simply didn't load as expected and upon investigation this is what it was shown:

![screenshot of cloudinary profile image bug](repo_images/cloudinary_bug.png)

# Models
## Profile Model:
The Profile model represents user profiles and contains information such as the owner, creation and update timestamps, name, bio, and image.

Fields:
- owner: One-to-One relationship field linking to the User model, representing the owner of the profile.
- created_at: DateTimeField automatically set to the current date and time when the profile is created.
- updated_at: DateTimeField automatically updated to the current date and time whenever the profile is modified.
- name: CharField with a maximum length of 255 characters, allowing for an optional name for the profile.
- bio: TextField allowing for an optional bio or description for the profile.
- image: ImageField specifying the location where profile images are uploaded. It uses the 'images/' directory as the upload      destination and has a default image specified as '../default_profile_xyw4hp'.

![screenshot of profile model](repo_images/profile_model.png)

The Meta class within the Profile model specifies the ordering of profile instances based on their creation timestamps. Profiles are ordered in descending order by created_at.

The model includes a __str__ method that returns a string representation of the profile, indicating the owner's username.

A create_profile function is defined as a signal receiver and connected to the post_save signal of the User model. This function automatically creates a profile for a newly created user.

## Post model:
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

## Review Model: 
The Review model represents reviews related to users and posts. Each review contains information such as the owner, post, creation and update timestamps, and content.

Fields:
- owner: ForeignKey field linking to the User model, representing the owner of the review.
- post: ForeignKey field linking to the Post model, representing the post associated with the review.
- created_at: DateTimeField automatically set to the current date and time when the review is created.
- updated_at: DateTimeField automatically updated to the current date and time whenever the review is modified.
- content: TextField representing the content or text of the review.

The Meta class within the Review model specifies the ordering of review instances based on their creation timestamps. Reviews are ordered in descending order by created_at.

The model includes a __str__ method that returns a string representation of the review, displaying the review's content.

# Serializers

## Profile Serializer
The ProfileSerializer is responsible for serializing and deserializing data related to the Profile model. It defines how the Profile instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the profile owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the profile.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Profile model. The specified fields include: id, owner, created_at, updated_at, name, bio, image, and is_owner.

## Post Serializer

The PostSerializer is responsible for serializing and deserializing data related to the Post model. It defines how the Post instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the post owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the post.
- profile_id: A read-only field that represents the ID of the owner's profile.
- profile_image: A read-only field that represents the URL of the owner's profile image.

The serializer also includes a method called validate_image to validate the size and dimensions of the image field. It ensures that the image size is not larger than 2MB and that the height and width do not exceed 4096 pixels.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Post model. The specified fields include: id, owner, profile_id, profile_image, created_at, updated_at, title, author, content, image, is_owner, genre_filter, and image_filter.

## Review Serializer
The ReviewSerializer is responsible for serializing and deserializing data related to the Review model. It defines how the Review instances are represented in JSON format.

The serializer includes the following fields:
- owner: A read-only field that represents the username of the review owner.
- is_owner: A custom field that determines whether the authenticated user is the owner of the review.
- profile_id: A read-only field that represents the ID of the owner's profile.
- profile_image: A read-only field that represents the URL of the owner's profile image.

The serializer's Meta class defines the model and fields that should be included in the serialized representation of the Review model. The specified fields include: id, owner, post, profile_id, profile_image, created_at, updated_at, content, and is_owner.

### Review Detail Serializer
The ReviewDetailSerializer is a subclass of ReviewSerializer and is used specifically for the detail view of a review. It adds an additional field:
- post: A read-only field that represents the ID of the associated post.


# API Views 

## ReviewList APIView
The ReviewList APIView provides an API endpoint for listing and creating reviews.

GET: Retrieve a list of all reviews.
- Endpoint: /reviews/
- Method: GET
- Permissions: Requires authentication or allows read access to unauthenticated users.
- Response: Returns a JSON response containing the serialized data of all reviews.

POST: Create a new review.
- Endpoint: /reviews/
- Method: POST
- Permissions: Requires authentication.
- Request: Accepts a JSON payload containing the review data.
- Response: Returns a JSON response containing the serialized data of the created review if the data is valid. If the data is invalid, returns a JSON response with the serializer errors.

## ReviewDetail APIView
The ReviewDetail APIView provides an API endpoint for retrieving, updating, or deleting a specific review.

GET: Retrieve a specific review by its ID.
- Endpoint: /reviews/{id}/
- Method: GET
- Permissions: Requires authentication or allows read access to unauthenticated users.
- Response: Returns a JSON response containing the serialized data of the specified review.

PUT: Update a specific review by its ID.
- Endpoint: /reviews/{id}/
- Method: PUT
- Permissions: Requires authentication and only accessible by the owner of the review.
- Request: Accepts a JSON payload containing the updated review data.
- Response: Returns a JSON response containing the serialized data of the updated review if the data is valid. If the data is invalid, returns a JSON response with the serializer errors.

DELETE: Delete a specific review by its ID.
- Endpoint: /reviews/{id}/
- Method: DELETE
- Permissions: Requires authentication and only accessible by the owner of the review.
- Response: Returns a JSON response with a success message if the review is deleted successfully.
