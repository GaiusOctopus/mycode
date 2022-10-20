#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Famous Landmarks Mini-Project """

def main():
    
    # create dictionary of landmarks and attributes
    landmark= {
                "Angkor Wat": {
                    "location": "Siem Reap, Cambodia",
                    "description": "This expansive temple complex is one of Southeast Asia's most significant archeological sites built by Khmer Empire."
                             },
                "Sydney Opera House": {
                    "location": "Sydney, Australia",
                    "description": "One of Australia's top tourist attractions. Also known as one of the busiest performing arts venues in the world."
                                      },
                "Eiffel Tower": {
                    "location": "Paris, France",
                    "description": "Built for the International Exposition of 1889, this served as the entrance gateway to the exposition."
                                },
                "Taj Mahal": {
                    "location": "Agra, India",
                    "description": "Built as tribute to the favorite wife of Mughal Emperor Shah Jahan."
                             },
                "Burj Khalifa": {
                    "location": "Dubai, United Arab Emirates",
                    "description": "This is the tallest building and tallest free-standing structure in the world."
                                }
              }
   
    # convert landmark dictionary to list for indexing 
    # [('Ankor Wat', {'Location': 'Siem Reap, Cambodia', 'Description"': "This expansive temple complex is one of Southeast Asia's most significant archeological sites built by Khmer Empire."}), ('Sydney Opera House', {'Location': 'Sydney, Australia', 'Description': "One of Australia's top tourist attractions. Also known as one of the busiest performing arts venues in the world."}), ('Eiffel Tower', {'Location': 'Paris, France', 'Description': 'Built for the International Exposition of 1889, this served as the entrance gateway to the exposition.'}), ('Taj Mahal', {'Location': 'Agra, India', 'Description': 'Built as tribute to the favorite wife of Mughal Emperor Shah Jahan.'}), ('Burj Khalifa', {'Location': 'Dubai, United Arab Emirates', 'Description': 'This is the tallest building and tallest free-standing structure in the world.'})]

    landmark_list= list(landmark.items())

    print("Let's play guess the landmark!")

    print(landmark_list[0]["description"])

if __name__ == "__main__":
    main()
