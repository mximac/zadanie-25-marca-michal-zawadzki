def setup():
    size(400,400)
    textSize(70)
def draw():
    background(0)
    text("M", width/2-50, height/2)
    text("Z", width/2+20, height/2)
    fill(155)
    print(mouseX,mouseY)
    if keyPressed:
        fill(155)
        if key == 'Z' or key == 'z':
            fill(255, 0, 0)
            text("Z", width/2+20, height/2)
            fill(155)
    if keyPressed:
        fill(155)
        if key == 'M' or key == 'm':
            fill(255, 0, 0)
            text("M", width/2-50, height/2)
            fill(155)
    if (mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200):
        text("Z", width/2+20, height/2)
        fill(0, 102, 153)
        if keyPressed:
            if keyCode == 39 and mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200: #strzalka w prawo i myszka na M
                fill(255, 0, 0)
                text("Z", width/2+20, height/2)
                fill(155)
                print(keyCode)
    if (mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200):
        text("M", width/2-50, height/2)
        fill(0, 102, 153)
        if keyPressed:
            fill(155)
            if keyCode == 37 and mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200: #strzalka w lewo i myszka na Z
                fill(0, 255, 0)
                text("M", width/2-50, height/2)
                fill(155)
                print(keyCode)
    s=createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.noStroke()
    s.vertex(150, 200)
    s.vertex(200, 250)
    s.vertex(200, 200)
    s.vertex(150, 250)
    s.endShape(CLOSE)
    shape(s, 25, 25)
