import moviepy.editor as mp

def merge_two_clips(clip1: str, clip2: str):
  clip1 = mp.VideoFileClip(clip1)
  clip2 = mp.VideoFileClip(clip1)
  resolution1 = clip1.size
  resolution2 = clip2.size
  target_resolution = (max(resolution1[0], resolution2[0]), max(resolution1[1], resolution2[1]))
  clip1_resized = clip1.resize(newsize=target_resolution)
  clip2_resized = clip2.resize(newsize=target_resolution)
  final_clip = mp.concatenate_videoclips([clip1_resized, clip2_resized])
  final_clip.write_videofile("combined_high_res.webm", codec='libvpx-vp9', preset='slow')

  return 'Clips Combined Successfully With Name combined_high_res.webm'
