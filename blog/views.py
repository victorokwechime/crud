from django.shortcuts import render

PostListView
model = Post

PostCreateView
model = Post

fields = “__all__”

success_url  = reverse_lazy(“blog:all”)

PostDetailView
model = Post

PostUpdateView
model = Post

fields = “__all__”

success_url  = reverse_lazy(“blog:all”)

PostDeleteView 
model = Post

fields = “__all__”

success_url  = reverse_lazy(“blog:all”)