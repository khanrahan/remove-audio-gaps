'''
Script Name: Remove Audio Gaps
Written By: Kieran Hanrahan

Script Version: 1.0.0
Flame Version: 2021.1

URL: http://github.com/khanrahan/remove-audio-gaps

Creation Date: 1.10.24
Update Date: 1.10.24

Description:

    Remove gaps on the audio tracks.

Menus:

    Right-click selected items on the Desktop --> Edit... --> Remove Audio Gaps
    Right-click selected items in the Media Panel --> Edit... --> Remove Audio Gaps

To Install:

    For all users, copy this file to:
    /opt/Autodesk/shared/python

    For a specific user, copy this file to:
    /opt/Autodesk/user/<user name>/python
'''

from __future__ import print_function
import flame


TITLE = 'Remove Audio Gaps'
VERSION_INFO = (1, 0, 0)
VERSION = '.'.join([str(num) for num in VERSION_INFO])
TITLE_VERSION = '{} v{}'.format(TITLE, VERSION)
MESSAGE_PREFIX = '[PYTHON]'


def message(string):
    '''Print message to shell window and append global MESSAGE_PREFIX.'''

    print(' '.join([MESSAGE_PREFIX, string]))


def remove_audio_gaps(sequence):
    '''Loop through all the audio tracks and remove any audio gaps.'''

    for audio_track in sequence.audio_tracks:
        for track in audio_track.channels:
            for item in track.segments:
                if item.name == '':  # no name indicates audio gap
                    flame.delete(item)


def process_selection(selection):
    ''' '''

    message(TITLE_VERSION)
    message('Script called from {}'.format(__file__))

    for sequence in selection:
        remove_audio_gaps(sequence)

    message('Done!')


def scope_sequence(selection):
    '''Filter for only PySequence.'''

    for item in selection:
        if isinstance(item, flame.PySequence):
            return True
    return False


def get_media_panel_custom_ui_actions():
    '''Python hook to add custom right click menu.'''

    return [{'name': 'Edit...',
             'actions': [{'name': 'Remove Audio Gaps',
                          'isVisible': scope_sequence,
                          'execute': process_selection,
                          'minimumVersion': '2023'}]
            }]
