class Dog:
    def __init__(self, id, breed, color, age_span):
        self.id = id
        self.breed = breed
        self.color = color
        self. age_span = age_span

    def to_dict(self):
        return dict(
            id=self.id,
            breed=self.breed,
            color=self.color,
            age_span=self.age_span
        )

dogs = [ 
    Dog(1, "Labrador Retriever", "Yellow", "10-12 years"),
    Dog(2, "German Shepherd", "Black and Tan", "9-13 years"),
    Dog(3, "Golden Retriever", "Golden", "10-12 years"),
    Dog(4, "Bulldog", "Brindle", "8-10 years"),
    Dog(5, "Beagle", "Tri-color", "12-15 years"),
    Dog(6, "Poodle", "White", "12-15 years"),
    Dog(7, "Rottweiler", "Black and Mahogany", "8-10 years"),
    Dog(8, "Yorkshire Terrier", "Blue and Tan", "13-16 years"),
    Dog(9, "Dachshund", "Red", "12-16 years"),
    Dog(10, "Siberian Husky", "Gray and White", "12-15 years")
    ]