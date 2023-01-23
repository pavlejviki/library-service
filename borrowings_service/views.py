from django.shortcuts import render

@login_required
def add_borrowing(request):
    if request.method == 'POST':
        # Get the book and user from the request
        book_id = request.POST.get('book_id')
        user = request.user

        # Get the book from the database
        book = Book.objects.get(id=book_id)
        # check the inventory and if it's 0 or less return a message
        if book.inventory <= 0:
            return render(request, 'error.html', {'error_message': 'This book is not available for borrowing'})
        # Create a new borrowing
        borrowing = Borrowing(book=book, user=user, borrow_date=datetime.date.today(), expected_return_date=datetime.date.today() + datetime.timedelta(days=14))
        borrowing.save()
        # Update the book inventory
        book.inventory -= 1
        book.save()
        return redirect('borrowings')
    else:
        # Handle GET request
        pass

@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    """Get a random character from Rick and Morty world"""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)