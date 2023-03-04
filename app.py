from flask import Flask, render_template, jsonify, redirect
import re
app = Flask(
    __name__, 
    static_folder='statics',
    static_url_path='',
    template_folder='templates'
)

@app.route('/')
def main():
    return redirect('/chapter/1')

@app.route('/chapter/<chapter>', methods=['GET'])
def request(chapter):
    with open(f'./assets/Chapters/Journey to the West [Chapter {chapter}].txt', 'rb') as file:
        chapter = int(chapter)
        contents = file.read()
        # contents = re.split('\n+', contents.decode())
        contents = contents.decode().split("\n")
        cnt = []
        for content in contents:
            if content.strip() == '':
                if not contents[contents.index(content) - 1].endswith('.'):
                    pass
                else:
                    cnt.append('<p></p>')
            else:
                cnt.append(f"<p>{content}</p>")
        contents = ''.join(cnt)       
        # contents = ''.join([f"<p>{content}</p>" if not content.strip() == '' else "<p></p>" for content in contents])
        prev = chapter - 1
        next_ = chapter + 1
        if chapter == 1:
            prev = ''
        if chapter == 100:
            next_ = ''
        return render_template('index.html', data = [contents, f'Chapter {chapter}', prev, next_])

if __name__ == '__main__':
    app.run(debug=True)