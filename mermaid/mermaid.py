import base64
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

def mm(graph):
    graphbytes = graph.encode("utf8")
    base64_bytes = base64.urlsafe_b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    url = "https://mermaid.ink/img/" + base64_string
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    plt.imshow(img)
    plt.axis("off")
    plt.show()


def flow_chart():
    graph = """
            graph TD;
              A-->B;
              A-->C;
              B-->D;
              C-->D;
          """
    mm(graph)


def mind_map():
    graph = """

            mindmap
              root((mindmap))
                Origins
                  Long history
                  ::icon(fa fa-book)
                  Popularisation
                    British popular psychology author Tony Buzan
                Research
                  On effectiveness<br/>and features
                  On Automatic creation
                    Uses
                        Creative techniques
                        Strategic planning
                        Argument mapping
                Tools
                  Pen and paper
                  Mermaid

          """
    mm(graph)


def sequence_diagram():
    graph = """
              sequenceDiagram
                  participant Alice
                  participant Bob
                  Alice->>John: Hello John, how are you?
                  loop HealthCheck
                      John->>John: Fight against hypochondria
                  end
                  Note right of John: Rational thoughts <br/>prevail!
                  John-->>Alice: Great!
                  John->>Bob: How about you?
                  Bob-->>John: Jolly good!
              """
    mm(graph)


def sequence_diagram2():
    graph = """
            sequenceDiagram
              participant web as Web Browser
              participant blog as Blog Service
              participant account as Account Service
              participant mail as Mail Service
              participant db as Storage

              Note over web,db: The user must be logged in to submit blog posts
              web->>+account: Logs in using credentials
              account->>db: Query stored accounts
              db->>account: Respond with query result

              alt Credentials not found
                  account->>web: Invalid credentials
              else Credentials found
                  account->>-web: Successfully logged in

                  Note over web,db: When the user is authenticated, they can now submit new posts
                  web->>+blog: Submit new post
                  blog->>db: Store post data

                  par Notifications
                      blog--)mail: Send mail to blog subscribers
                      blog--)db: Store in-site notifications
                  and Response
                      blog-->>-web: Successfully posted
                  end
              end
            """
    mm(graph)


def user_journey():
    graph = """
            journey
              title My working day
              section Go to work
                Make tea: 5: Me
                Go upstairs: 3: Me
                Do work: 1: Me, Cat
              section Go home
                Go downstairs: 5: Me
                Sit down: 5: Me
          """
    mm(graph)

### Zen UML broken!
def zen_uml():
  graph = """
          zenuml
            title Demo
            Alice->John: Hello John, how are you?
            John->Alice: Great!
            Alice->John: See you later!
          """
  mm(graph)


def driver():
  sequence_diagram2()
