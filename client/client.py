import socket

def establish_connection(host, port):
 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def display_main_menu():
    
    print("Main Menu:")
    print("1. Search headlines")
    print("2. List of Sources")
    print("3. Quit")

def display_headlines_menu():
  
    print("Headlines Menu:")
    print("1. Search for keywords")
    print("2. Search by category")
    print("3. Search by country")
    print("4. List all news headlines")
    print("5. Back to the main menu")

def display_sources_menu():
   
    print("Sources Menu:")
    print("1. Search by category")
    print("2. Search by country")
    print("3. Search by language")
    print("4. List all sources")
    print("5. Back to the main menu")

def main():
    host = '127.0.0.1'   
    port = 9000   

    client_socket = establish_connection(host, port)
    username = input("Enter your username: ")
    client_socket.send(username.encode())   

    while True:
        display_main_menu()
        choice_main = input("Enter the number of your choice: ")
        client_socket.send(choice_main.encode())  

        if choice_main == '1':
            
            display_headlines_menu()
            choice_headlines = input("Enter the number of your choice: ")
            client_socket.send(choice_headlines.encode())   

        elif choice_main == '2':
           
            display_sources_menu()
            choice_sources = input("Enter the number of your choice: ")
            client_socket.send(choice_sources.encode())  
         

        elif choice_main == '3':
            print("Goodbye!")
            client_socket.send(choice_main.encode())   
            client_socket.close()   
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
