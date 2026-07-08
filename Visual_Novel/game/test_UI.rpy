################################################################################
## Test UI
################################################################################
##
## Separate preview screen for the custom dialogue layout.
## This does not replace the default say screen in screens.rpy.

screen test_ui_say(who, what):

    vbox:
        xalign 0.5
        yalign 1.0
        spacing 20

        add "test_images/Middle_char.webp":
            xalign 0.5
            ysize 620

        hbox:
            xalign 0.5
            spacing 32

            fixed:
                xsize gui.textbox_height
                ysize gui.textbox_height

                add "test_images/left_char.webp":
                    xalign 0.5
                    yalign 0.5
                    ysize gui.textbox_height

            window:
                style "test_ui_say_window"

                if who:
                    window:
                        style "test_ui_namebox"
                        text who style "test_ui_say_label"

                text what style "test_ui_say_dialogue"

            fixed:
                xsize gui.textbox_height
                ysize gui.textbox_height

                add "test_images/right_char.webp":
                    xalign 0.5
                    yalign 0.5
                    ysize gui.textbox_height


screen test_ui_preview():

    tag menu

    add Solid("#000")

    use test_ui_say("Test", "This is a test dialogue box. Check the left image, dialogue box, and right image alignment.")

    textbutton "Back":
        xalign 0.98
        yalign 0.03
        action Return()


label test_ui_preview:

    call screen test_ui_preview
    return


style test_ui_say_window is window
style test_ui_namebox is namebox
style test_ui_say_label is say_label
style test_ui_say_dialogue is say_dialogue

style test_ui_say_window:
    xfill False
    xsize 1600
    ysize gui.textbox_height
    yalign 0.5

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style test_ui_namebox:
    xpos 40
    xanchor 0.0
    xsize None
    ypos 10
    ysize None

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=0.0)
    padding gui.namebox_borders.padding

style test_ui_say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    yalign 0.5

style test_ui_say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 80
    xsize 1440
    ypos 95

    adjust_spacing False
