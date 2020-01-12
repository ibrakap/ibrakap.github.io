---
layout: post
title: "How to make cool launchers in Godot engine?"
date: 2019-10-01
categories:
---
# How to make cool launchers in Godot engine?
Hello everyone. First of all, I want thank to [bruvzg](https://github.com/bruvzg) for [per-pixel transparency](https://github.com/godotengine/godot/pull/14622) contribution. I will show how to make cool launchers in Godot engine.<br>Your image must contain an alpha channel for providing per-pixel transparency. Let’s make that. For using per-pixel transparency you need to enable these settings. Follow that step.
<br>

```
Project -> Project Settings -> General -> Display -> Window -> Per Pixel Transparency
```
<br>
later enable these

 - Allowed
 - Enabled
 - Splash

<br>
<img src="../../../../images/1 X4BKQGClSZTgWn7Ut6bYVQ.png" alt="drawing" width="900" height="600"/>
<br>
After creating a control node and add TextureRect node for a background image. Set an image to TextureRect node later align it where you want. I prefer in center of screen.
<br>
<img src="../../../../images/1 gIp9wt59xmP3HlZYPuSjUA.png" alt="drawing" width="900" height="600"/>
<br>
Later add a script to Control node. Later write this code under the _ready method for frame transparency because Godot comes with their own defult gray background.
<br>
```gdscript
get_tree().get_root().set_transparent_background(true)
```
<br>
Finally our image successfully visible without gray background.
<br>
<img src="../../../../images/1 N2F4G-WnBHd6bxFQ_qm3tg.png" alt="drawing" width="900" height="600"/>
<br>
This frame is not draggable with the mouse. If you want to add drag and drop functionality to your frame. Add gui_input signal to control node. Later define those variables for moveability.
<br>
```gdscript
var drag = Vector2()
var follow = false
```
<br>
Later write that code under gui_input method.
<br>
```gdscript
if event is InputEventMouseButton:
  if event.get_button_index() == 1:
   follow = !follow
   drag = get_local_mouse_position()
```
<br>
Later write that code under _process method.
<br>
```gdscript
if follow:
  OS.set_window_position(OS.window_position + get_global_mouse_position() - drag)
```
<br>
Finally we can drag and drop our background image while runtime.
Let’s add a button on image to load the scene.
<br>
<img src="../../../../images/1 wkQWMMZxjXEmtFngHguSPA.png" alt="drawing" width="900" height="600"/>
<br>
Add button signal to control node and write the code given below for load scene.
<br>
```gdscript
OS.window_borderless = false
get_tree().get_root().set_transparent_background(false)
get_tree().change_scene("res://testscence.tscn")
``` 
<br>
Thanks for reading my article. If you want download this project. You can access it [here](https://github.com/ibrakap/GodotCoolLauncher).
<br>
Used resources:
[https://github.com/godotengine/godot/pull/14622](https://github.com/godotengine/godot/pull/14622)
[https://www.youtube.com/watch?v=alKdkRJy-iY](https://www.youtube.com/watch?v=alKdkRJy-iY) Thanks Emilio for awesome tutorials.
