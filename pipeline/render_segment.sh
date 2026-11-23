#!/bin/bash
# Cắt 1 đoạn từ source, chuẩn hoá 1080x1920@30, encode (không làm đẹp — chủ kênh đã bỏ bước này).
# usage: render_segment.sh <work_dir> <n> <src_name> <start> <dur> <zoom>
#   zoom: 0 = đứng yên · 1 = zoom chậm 7% · 2 = zoom in 1.00→1.18 · 3 = zoom out 1.18→1.00
W=$1; n=$2; src=$3; ss=$4; d=$5; z=$6
fit="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"
case "$z" in
  1) vf="fps=30,scale=w='trunc(1080*(1+0.07*t/$d)/2)*2':h='trunc(1920*(1+0.07*t/$d)/2)*2':eval=frame,crop=1080:1920" ;;
  2|3)
    if [ "$z" = 2 ]; then k="(1+0.18*(1-pow(1-on/($d*30),2)))"; else k="(1.18-0.18*(1-pow(1-on/($d*30),2)))"; fi
    vf="fps=30,$fit,scale=2160:3840,zoompan=z='$k':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30" ;;
  *) vf="fps=30,$fit" ;;
esac
mkdir -p "$W/seg"
ffmpeg -v error -y -ss "$ss" -t "$d" -i "$W/src/$src" -an -vf "$vf" -frames:v $(python3 -c "print(round($d*30))") \
  -c:v libx264 -preset fast -crf 17 -pix_fmt yuv420p "$W/seg/$n.mp4"
echo "seg $n done $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$W/seg/$n.mp4")"
