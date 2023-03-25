for book_rating in books:
    rating_element = book_rating.find("p", class_="star-rating Three")
    title_element = book_rating.find_element_by_path( )
    price_element = book_rating.find("div", class_="product_price")
    print(rating_element.text.strip())
    print(title_element.text.strip())
    print(price_element.text.strip())
    print()