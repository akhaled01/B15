# About the `HTTP` Module

Our project is a quite different due to a multitude of factors, the biggest of which, is that it's compliant with the [HTTP/1.1 RFC](https://https://datatracker.ietf.org/doc/html/rfc2616).

> [!NOTE]
> `nginx` has inspired the idea of this project!

The hypertext transfer protocol is an application-level protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web. It is a OSI Layer 7 Protocol built on top of a OSI Layer 4 protocol (TCP).

The idea of this module, is to provide our TCP server socket the ability to accept HTTP clients from any source, and that is done by making it understand the requests, and encode responses in a very specific manner.

Going through the module, you'll find a module called `HttpRequest` and `HTTPResponseWriter` that facilitate communication with all client. You'll also find the Router function that is responsible
for multiplexing the requests to the required controller.
