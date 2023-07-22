
size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

x = width / 2
y = height / 2

r2 = 140

arc(
  x, y,
  r2, r2,
  0, 2, PIE
)



p214 = PI*2/14

# vacation
fill('#00FF00')
arc(x, y, r2*4, r2*4, p214*11, p214*12, PIE)


# metal
fill('#FF99FF')
arc(x, y, r2*3, r2*3, PI, p214*9, PIE)


# rap
fill('#FF99FF')
arc(x, y, r2*3, r2*3, p214*9, p214*11, PIE)

# photos
fill('#0099FF')
arc(x, y, r2*3, r2*3, p214*11, p214*13, PIE)


# work
fill('#0099FF')
arc(x, y, r2*3, r2*3, p214*13, p214*14, PIE)


# video
fill('#FF0000')
arc(x, y, r2*2, r2*2, 0, PI, PIE)

# music
fill('#FF3399')
arc(x, y, r2*2, r2*2, PI, p214*11, PIE)


# docs
fill('#6633FF')
arc(x, y, r2*2, r2*2, p214*11, p214*14, PIE)


# center
fill('#004477')
circle(x, y, r2)
