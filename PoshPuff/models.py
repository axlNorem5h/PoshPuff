from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='Php')

    def __str__(self):
        return f"{self.product.name} - {self.price} {self.currency}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)  # You might want to use a ForeignKey to a User model
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100)  # You might want to use a ForeignKey to a User model
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.post.title} - {self.created_at}"
