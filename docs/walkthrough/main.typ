// modified from 
// minimal-presentation:0.1.0
#import "lib.typ": *
#import "@preview/cetz:0.3.1": canvas, draw, vector, matrix
#import "@preview/fletcher:0.5.2" as fletcher: diagram, node, edge
#import fletcher.shapes: house, hexagon, diamond, triangle

#set text(font: "Montserrat")
#set figure(supplement: "Figure", numbering: "1")
#let diagram(..args) = {
  set text(black)
  fletcher.diagram(..args)
}
#let newplasma = array(())
#{
  let prevcolor = none
  for color in color.map.plasma{  
    if prevcolor == none {prevcolor = color; continue}

    let gradation = 10
    for i in range(gradation) {
      let j = i * (100/gradation)
      newplasma.push(
        color.mix((prevcolor, 100-j), (color, j),).darken(10%)
      )
    }
    prevcolor = color
  }
}
#let themegradientcolour = array(())
#for color in (..newplasma, ..newplasma, ..newplasma, ..newplasma) {
  themegradientcolour.push(color)
}

#let counter = 0

#show: project.with(
  title:  align(top+center)[#v(1em)#text(size: 70pt)[STELLA]\ #v(-0.75em)#text(tracking: 1pt, size:14pt)[Simulated Training Environments\ #v(-5pt)and Large Learning Automata]],
  sub-title: align(left)[#v(3em) Project Walkthrough],
  author: "SE 4450",
  date: "Team 32",
  index-title: "Summary",
  logo: text(size: 20pt)[STELLA],
  logo-light: none,
  cover: image("images/juliaset2.png"),
  background: rect(width: 100%, height: 100%, fill: gray.darken(85%)),//image("./image_1.jpg"),
  cover-color: gradient.conic(..color.map.rainbow, angle: -100deg, center: (40%, 50%)),
  main-color: gradient.conic(..themegradientcolour, angle: -90deg,center: (-20%, -20%)),
  corner-color: gradient.conic(..color.map.plasma, angle: -20deg),
)

/*

put content below

*/

= Project Summary and Targets

== STELLA
#columns-content()[
  - STELLA is an implementation of a autonomous driving agent trained in simulations
  
  - The project will adapt recent techniques into a usable framework and tools for others to adapt and use.
  
    - while also reproducing and verifying those published results 
][
  #figure(
    image("images/1.png", width: 100%),
    caption: [Autonomous vehicle in the CARLA simulator],
  )
]

=== Project Goals
/*
- what we want to complete  
  - be reasonable
- build an agent
- evaluation
  - AV MAP and Sensors track
- FOSS contributions
*/
#columns-content()[
  #figure(caption: [Data flow visualization],
    image("images/tf.png", ))
][
- The main goal is to build a working autonomous agent based off of the CarLLaVA technique by Renz et al @renz2024

- In the process, many tools may need to be built or adapted

- The final agent also needs to be evaluated through a variety of different metrics to compare with other frameworks and techniques
]

=== FOSS
- While the techniques we are adapting are published for reading, the source code has not been released so there are no available implementations or reproductions of this work yet

- The project will rely on a variety of free and open source tools

- In return, the project hopes to help improve these open source tools that we use through
  - better documentation
  - bug finding and fixing
  - feature additions 

= Methodology

== Workflow and Structures

#let blob(pos, label,width: 45mm, tint: white, radius: 5pt, ..args) = node(
	pos, align(center, label),
	width: width,
	fill: tint.lighten(60%),
	stroke: 1pt + tint.darken(20%),
	corner-radius: radius,
	..args,
)

#columns-content[
- Setup simulator and development environment 
- Collect training data
- Build initial agent
- Train, test, repeat
][
  #figure(caption: "Workflow",
  [
  #text(black, size: 20pt)[
  #diagram(
  spacing: 8pt,
  cell-size: (10mm, 15mm),
  edge-stroke: 1pt + white,
  edge-corner-radius: 5pt,
  mark-scale: 70%,
  blob((-1.5,-1.5), [Setup Workspace], tint: blue,radius: 20pt),
  edge("-|>"),
  blob((-1.5,0), [Build Agent], tint: blue,radius: 20pt),
  blob((0.5,-1.5), [Data Collection], tint: blue,radius: 20pt),
  edge("-|>"),
  blob((0.5,0), [Training and Validation], radius: 20pt, tint: orange),
  edge("-|>"),
  edge((-1.5, 0), (0.5, 0),"-|>"),
  blob((0.5,1), [Testing], tint: green,radius: 20pt),
  edge("-|>"),
  blob((0.5,2), [Iterate], tint: red,radius: 20pt),
  edge((0.5, 2), (0, 2), "rr", "uu", "l", "-|>"),
)
]])

]

=== Training Data Collection / Generation
#columns-content[
  #figure(caption: "Data Collection",
  diagram(
  spacing: 8pt,
  cell-size: (10mm, 15mm),
  edge-stroke: 1pt + white,
  edge-corner-radius: 5pt,
  mark-scale: 70%,
  blob((-2,2), [Scenarios], tint: blue,),
  blob((0,3), [Collected Data], tint: green,shape: hexagon),
  edge("<|-"),
  edge((-2,2), (0,2), "-|>"),
  blob((0,2), [CARLA], radius: 20pt, tint: orange),
  edge("<|-"),
  blob((0,1), [Rule Based Expert], tint: red)
))][
  - Follows the dataset generation method in Renz et al @renz2024
  - Rule based experts are allowed to cheat, directly sourcing exactly where other vehicles are in the simulation
  - Relies on branching decision trees, rather than adaptive machine learning methods
    - more consistent at specific scenarios but worse at handling edge cases
]
=== Training
#columns-content[
    - The collected data is then used to fine tune a pretrained model
    - The pretrained CarLLaVA model has already trained on a few million images of common objects, so it has some built in intuition already
][
  #figure(caption: "Training",
diagram(
  spacing: 8pt,
  cell-size: (10mm, 15mm),
  edge-stroke: 1pt + white,
  edge-corner-radius: 5pt,
  mark-scale: 70%,
  blob((-2,2), [Pretrained CarLLaVA Model], tint: blue,),
  blob((0,1), [Collected Data], tint: green,),
  edge("-|>"),
  edge((-2,2), (0,2), "-|>"),
  blob((0,2), [Fine Tuning], width: 55mm, radius: 20pt, tint: orange),
  edge("-|>"),
  blob((0,3), [Trained Model], tint: red)
))]

=== Autonomous Agent Internals

#columns-content[
    - The CarLLaVA model handles decision making and visual processing
    - the agent then forwards the output waypoints to a proportional, integral, derivative (PID) controller 
      - combined with GPS data to complete its navigation  
][
  #figure(caption: "Agent Structure",
diagram(
  spacing: 8pt,
  cell-size: (10mm, 15mm),
  edge-stroke: 1pt + white,
  edge-corner-radius: 5pt,
  mark-scale: 70%,
  blob((-2,2), [Vision Data], tint: blue,),
  blob((0,1), [Path and Trajectory], tint: green,),
  edge("-|>"),
  edge((-2,2), (0,2), "-|>"),
  blob((0,2), [CarLLaVA], width: 55mm, radius: 20pt, tint: orange),
  edge("-|>"),
  blob((0,3), [Waypoints],shape: hexagon, tint: green),
  edge("-|>"),
  blob((0,4), [PID \ controller],radius: 1pt, tint: red)
))]
== PID Control
  - PID is an algorithm for smooth transitions towards a target point using a scalar feedback value (error $e$)#footnote(text(size: 13pt)[Several of our team members have experience with PID through robotics])
  - This can be combined with GPS data to align vehicle over designated waypoints
  #grid(columns: (1fr, 1.2fr), [
  $ "PID"(e,t) = k_p e + k_i integral_0^t e space d t + k_d (d e)/(d t) $
  ],[
    #figure(caption: "Oscillation Dampening Using PID control",
      grid(columns: (1fr, 1fr),
        align: (right, left),
        image("images/P.png", fit: "cover", height: 25%),
        //image("I.png", fit: "cover", width: 100%),
        image("images/D.png", fit: "cover", height: 25%),
      )
  )],
)

== CarLLaVa
#grid(columns: (1.4fr, 1fr),
[
  #figure(caption: "CarLLaVA",
    image("images/Untitled.png", height: 100%,)
  )
],[
  - CarLLaVA utilises vision encoders to embed image information in a latent vector space
  - These features are then passed to the LLaMA transformer, which combines that with query, target, and status information to generate new GPS waypoints to follow
]
)
=== Vision Encoding
#align(center)[#figure(caption: "Vision Encoding ",image("images/latent.png", height: 100%))]
=== Vision Encoding
- Vision encoding maps images to some $n$ dimensional linear space, known as a latent vector space @spectral
- Related images will map onto manifolds (surfaces) in this space
  - specifically, the cosine similarity of encodings should be maximised when the images are similar 

  $ "Encode"("image") = vec(delim: "[", a_1, dots.v, a_n) quad quad quad  "cosine similarity" = cos (theta) = (A dot B)/(||A||||B||) $
=== Vision Encoding

#grid(columns: (2fr, 2fr), [#move(dx: -1em)[#figure(caption: "Encodings of Cat Pictures", image("images/cat.png", width: 100%))]],
 [
   -  Augmentations of the same photo should be very close to each other
  - Photos of dogs map to the same surface, and the same is true for cats. 
    - In reality, the manifold for any category will have a dimension much higher than 2
]
)
== Tools / Frameworks
#align(center)[
#grid(rows: 1fr, columns: (1fr, 1fr, 1fr),
[#image("images/CARLA.png", height: 100pt) CARLA], 
[#image("images/torch.png", height: 100pt)Pytorch], 
[#image("images/py.png", height: 100pt)Python],
[#image("images/wandb.png", height: 80pt)Weights  and Biases],
[#image("images/cuda.jpg", height: 80pt)CUDA],
[#image("images/hugging.png", height: 80pt)HuggingFace],
)]
== CarLLaVA is the State of the Art

#grid(columns: (2fr, 1fr),
[
  #figure(caption: "CARLA Leaderboard 2.0",
  image("images/chart.svg", height: 85%))
],[
  - Dominates the leaderboard
  - However, it has only been out for less than 6 months
])

== Modifications
- if there is enough time remaining, there are a number of modifications we want to attempt
#enum(
  [ViT with Registers
    - A study by Darcet et al @registers found a relatively simple modification that greatly improved the performance of ViT
  ],
  [
    Stereo vision
    - Internally, CarLLaVA already splits the visual field in two halves. Using two separate cameras, providing depth information may be useful to the model
  ]
)
=== ViT with Registers

#grid(columns: (1fr, 0.7fr), [
- Internally, the vision encoder in LLaVA is a form of vision transformer, or ViT
- ViT uses several transformer blocks chained sequentially
- Darcet et al.@registers added extra encoding dimensions (registers) to each block
  - and discarded them at the last layer
- Their model became much more robust, meaning that it based its decisions less on coincidences in the dataset and more on actual patterns 
],align(center)[
  #figure(caption: "Transformer Structure",
  image("images/transformer.png"))
])
=== Stereo Vision

- Stereo vision uses two cameras to guage depth and distance
- CarLLaVA's architecture seems to suggest it would naturally do well with information structured this way

#align(center)[
  #figure(caption: "Stereo Vision",
diagram(
  spacing: 8pt,
  cell-size: (10mm, 15mm),
  edge-stroke: 1pt + white,
  edge-corner-radius: 5pt,
  mark-scale: 70%,
  
  blob((0,3), [Left Camera], tint: blue,),
  blob((0.75,3), [Right Camera], tint: blue,),
  {
	let tint(c) = (stroke: c, fill: rgb(..c.components().slice(0,3), 5%),)
 
    node((0,5)," ", height: 60pt, width: 80mm,..tint(teal), shape: triangle)
    node((0.75,5)," ", height: 60pt, width: 80mm,..tint(teal), shape: triangle)
  },
))
]

= Measureable Outcomes

== Training Metrics
- We can measure how closely the model can emulate the behaviour of the rule-based expert through training metrics like accuracy and loss
- Often, the dataset is split into 2-3 sections
  - Training 
    - Trains the model, but represents the exact subset of data the model is familiar with
  - Evaluation
    - Used to periodically measure how generalizable the model is, and adjust hyperparameters
  - Test
    - Unseen by the model until the final evaluation, so that it only measures generalizability with no effect on the model itself
== CARLA Metrics
#columns-content[#figure(caption:"Unreal 4 CARLA", image("images/carlaheader.png", fit: "cover", height: 100%))
][
  - CARLA has 3 built in metrics
  - RC: Route completion
    - How much of a route was completed
  - IS: Infraction score
    - Negative score for infractions
  - DS: Driver score
    - Aggregated RC and IS score, with compensation for IS when achieving higher RC scores
]

== MAPS and SENSORS
#columns-content[
  - There are two commonly used tracks in CARLA, that contain a variety of scenarios and environments to navigate: MAPS and SENSORS
  - These are the two tracks used for leaderboards][
    #figure(caption: "Highway in CARLA", image("images/highway.png", height: 100%))
  ]

== References
#text(size: 18pt)[
*Literature*\
]
#{
v(-12pt)
show heading: it => {
}
set text(size: 12pt)
bibliography("refs.bib", style: "ieee", full: true, title: "")
}
#text(size: 18pt)[
*Image Sources*\
]
#v(-12pt)
#text(size: 12pt)[
https://www.youtube.com/watch?v=J4pHRM1Q5nQ\ 
https://blog.tensorflow.org/2024/02/graph-neural-networks-in-tensorflow.html\ 
https://arxiv.org/pdf/2406.10165\ 
https://arxiv.org/abs/2106.04156\
https://paperswithcode.com/sota/carla-leaderboard-2-0-on-carla\
https://arxiv.org/abs/1706.03762\
https://carla.org/
]
/*
example slides



= Leave slides below as examples until complete

= This is a section

== This is a slide title
#lorem(10)
- #lorem(10)
  - #lorem(10)
  - #lorem(10)
  - #lorem(10)

== One column image
#figure(
  image("images/image_1.jpg", height: 10.5cm),
  caption: [An image],
) <image_label>

== Two columns image

#columns-content()[
  #figure(
    image("images/image_1.jpg", width: 100%),
    caption: [An image],
  ) <image_label_1>
][
  #figure(
    image("images/image_1.jpg", width: 100%),
    caption: [An image],
  ) <image_label_2>
]

== Two columns

#columns-content()[
  - #lorem(10)
  - #lorem(10)
  - #lorem(10)
][
  #figure(
    image("images/image_1.jpg", width: 100%),
    caption: [An image],
  ) <image_label_3>
]

= This is a section

== This is a slide title

#lorem(10)

= This is a section

== This is a slide title

#v(-4em)
$ integral x d x  = x^2/2 + C $
#lorem(10)

= This is a section

== This is a slide title

#grid(columns: (1fr, 1fr), align: center, inset: 10pt , [#lorem(3)],[#lorem(3)],[abc], [def], [geh], [ijk])

= This is a very v v v v v v v v v v v v v v v v v v v v  long section

== slide in section


= sub-title test

== Slide title

#lorem(50)

=== Slide sub-title 1

#lorem(50)

=== Slide sub-title 2

#lorem(50)

== Slide title 2

#lorem(50)

=== Slide sub-title 3

#lorem(50)

=== Slide sub-title 4

#lorem(50)

== yipee

#set align(center)

#canvas({
  import draw: *

  // Set up the transformation matrix
  set-transform(matrix.transform-rotate-dir((1, 1, -1.3), (0, 1, .3)))
  scale(x: 1.5, z: -1)

  grid((0,-2), (8,2), stroke: gray.lighten(80%) + .5pt)

  // Draw a sine wave on the xy plane
  let wave(amplitude: 1, fill: none, phases: 2, scale: 8, samples: 100) = {
    line(..(for x in range(0, samples + 1) {
      let x = x / samples
      let p = (2 * phases * calc.pi) * x
      ((x * scale, calc.sin(p) * amplitude),)
    }), fill: fill)

    let subdivs = 8
    for phase in range(0, phases) {
      let x = phase / phases
      for div in range(1, subdivs + 1) {
        let p = 2 * calc.pi * (div / subdivs)
        let y = calc.sin(p) * amplitude
        let x = x * scale + div / subdivs * scale / phases
        line((x, 0), (x, y), stroke: rgb(50, 50, 50, 150) + .5pt)
      }
    }
  }

  group({
    rotate(x: 90deg)
    wave(amplitude: 1.6, fill: rgb(50, 50, 255, 100))
  })
  wave(amplitude: 1, fill: rgb(255, 50, 50, 100))
})

**/