from flask import Flask, jsonify, request

app = Flask(__name__) 

snippets = [
    {
      "id": 1,
      "language": "Python",
      "code": "print('Hello, World!')"
    },
    {
      "id": 2,
      "language": "Python",
      "code": "def add(a, b):\n    return a + b"
    },
    {
      "id": 3,
      "language": "Python",
      "code": "class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n\n    def area(self):\n        return 3.14 * self.radius ** 2"
    },
    {
      "id": 4,
      "language": "JavaScript",
      "code": "console.log('Hello, World!');"
    },
    {
      "id": 5,
      "language": "JavaScript",
      "code": "function multiply(a, b) {\n    return a * b;\n}"
    },
    {
      "id": 6,
      "language": "JavaScript",
      "code": "const square = num => num * num;"
    },
    {
      "id": 7,
      "language": "Java",
      "code": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"
    },
    {
      "id": 8,
      "language": "Java",
      "code": "public class Rectangle {\n    private int width;\n    private int height;\n\n    public Rectangle(int width, int height) {\n        this.width = width;\n        this.height = height;\n    }\n\n    public int getArea() {\n        return width * height;\n    }\n}"
    }
  ]

@app.route("/snippets", methods=["GET"])
def get_all_snippets():
    return jsonify(snippets)


if __name__ == '__main__':
    app.run(debug=True)
    
# curl -X POST -H "Content-Type: application/json" -d '{
# "id" : 9, 
# 'language': "C-",  
# 'code': 'Hello World'
# }' http://localhost:5000/snippets