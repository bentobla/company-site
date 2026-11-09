extends SceneTree
const App=preload('res://ui/app.gd')
var app
func _initialize():call_deferred('run')
func run():
 root.size=Vector2i(1080,2160)
 root.content_scale_size=Vector2i(432,864)
 root.content_scale_mode=Window.CONTENT_SCALE_MODE_CANVAS_ITEMS
 app=App.new()
 app.startup_splash=false
 app.profile_path='user://website-capture.json'
 for suffix in ['', '.tmp', '.bak']:DirAccess.remove_absolute(app.profile_path+suffix)
 root.add_child(app)
 app.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
 await process_frame
 await process_frame
 app.set_process(false)
 var languages={'de':'de-DE','en':'en-US','fr':'fr-FR','es':'es-ES','it':'it-IT','nl':'nl-NL','sv':'sv-SE','pl':'pl-PL','pt-br':'pt-BR','pt-pt':'pt-PT'}
 for language in languages:
  app.profile.settings.language=languages[language]
  app.profile.settings.theme='light'
  app._apply_theme()
  for scene in ['game','airports','briefing']:
   if scene=='game':
    app._start(app.content.mission('STR-3'),false)
    app.paused=true
    for tick in range(1100):
     if app.sim.status!='running':break
     app.sim.step()
    if not app.sim.aircraft.is_empty():app._select(app.sim.aircraft[0].id)
    app._game()
   elif scene=='airports':app._airports()
   else:
    app.profile.settings.theme='dark'
    app._apply_theme()
    app.chosen_mission='VLC-1'
    app._briefing()
   await process_frame
   await process_frame
   await RenderingServer.frame_post_draw
   var im=root.get_texture().get_image()
   if not im or im.is_empty():push_error('Empty screenshot');quit(1);return
   var folder='res://build/website/'+language
   DirAccess.make_dir_recursive_absolute(folder)
   im.save_png(folder+'/'+scene+'.png')
   print('SAVED ',language,'/',scene)
 app.queue_free()
 await process_frame
 quit()
