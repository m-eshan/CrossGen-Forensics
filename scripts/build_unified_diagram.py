import os
import zlib
import base64
import urllib.parse
import subprocess
from PIL import Image, PngImagePlugin

def build_drawio_xml():
    xml = """<mxfile host="app.diagrams.net" modified="2026-10-10T16:00:00.000Z" agent="Mozilla/5.0" version="24.0.0" type="device">
  <diagram id="CrossGen_Forensics_Architecture" name="CrossGen-Forensics Architecture">
    <mxGraphModel dx="1422" dy="854" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1640" pageHeight="980" background="#FFFFFF" adaptiveColors="none" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- CANVAS WHITE BACKGROUND CARD -->
        <mxCell id="bg_canvas" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E2E8F0;strokeWidth=1;arcSize=4;" vertex="1" parent="1">
          <mxGeometry x="20" y="20" width="1600" height="940" as="geometry" />
        </mxCell>

        <!-- TOP BANNER -->
        <mxCell id="banner" value="&lt;table width=&quot;100%&quot; style=&quot;color:#ffffff; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;tr&gt;&lt;td align=&quot;center&quot;&gt;&lt;div style=&quot;font-size:25px; font-weight:800; letter-spacing:-0.5px;&quot;&gt;&#128737;&#65039; CrossGen-Forensics&lt;/div&gt;&lt;div style=&quot;font-size:13px; color:#cbdcf7; font-weight:500; margin-top:5px; letter-spacing:0.2px;&quot;&gt;Multi-Generator Image Forensics &amp;nbsp;|&amp;nbsp; Cross-Architecture Learning &amp;nbsp;|&amp;nbsp; Generalization &amp;amp; Source Attribution&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0A3670;strokeColor=#0D438A;fontColor=#ffffff;arcSize=10;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1560" height="72" as="geometry" />
        </mxCell>

        <!-- ==================== LEFT: INPUT DATA ==================== -->
        <mxCell id="input_box" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:14.5px; font-weight:700; color:#0F172A;&quot;&gt;&#128452;&#65039; Input Data&lt;/div&gt;&lt;hr style=&quot;border:none; border-top:1px solid #BFDBFE; margin:8px 0;&quot;&gt;&lt;div style=&quot;font-size:12px; font-weight:700; color:#1E293B;&quot;&gt;Real &amp;amp; Generated Images&lt;/div&gt;&lt;br&gt;&lt;div style=&quot;font-size:11.5px; color:#334155; line-height:1.6;&quot;&gt;&#128444;&#65039; &lt;b style=&quot;color:#0F172A;&quot;&gt;ImageNet / Real&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;Authentic photographs&lt;/span&gt;&lt;br&gt;&lt;br&gt;&#9881;&#65039; &lt;b style=&quot;color:#0F172A;&quot;&gt;GAN-Generated&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;BigGAN synthetic images&lt;/span&gt;&lt;br&gt;&lt;br&gt;&#10024; &lt;b style=&quot;color:#0F172A;&quot;&gt;Diffusion Models&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;SD 2.1 / 3 / XL, DALL-E, MJ&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0F7FF;strokeColor=#3B82F6;strokeWidth=1.8;arcSize=8;verticalAlign=top;spacingTop=10;spacingLeft=10;spacingRight=10;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="40" y="130" width="220" height="730" as="geometry" />
        </mxCell>

        <!-- INPUT PILL BUTTON -->
        <mxCell id="input_pill" value="Raw Streams &amp;rarr;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DBEAFE;strokeColor=#93C5FD;strokeWidth=1;fontColor=#1D4ED8;fontSize=11.5;fontStyle=1;arcSize=20;" vertex="1" parent="1">
          <mxGeometry x="60" y="805" width="180" height="34" as="geometry" />
        </mxCell>

        <!-- ARROW: INPUT DATA -> STAGE 1 -->
        <mxCell id="arr_input_s1" value="" style="endArrow=classic;html=1;strokeWidth=2.5;strokeColor=#2563EB;exitX=1;exitY=0.12;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="input_box" target="stage1_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ==================== STAGE 1: DATA ACQUISITION & PREPROCESSING ==================== -->
        <mxCell id="stage1_box" value="&lt;div align=&quot;left&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif; font-size:14.5px; font-weight:700; color:#0F172A; padding-left:36px; padding-top:2px;&quot;&gt;Data Acquisition &amp;amp; Preprocessing&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0F7FF;strokeColor=#3B82F6;strokeWidth=1.8;arcSize=8;verticalAlign=top;align=left;spacingTop=8;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="280" y="130" width="1020" height="165" as="geometry" />
        </mxCell>

        <!-- BADGE 1 -->
        <mxCell id="b1" value="1" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#2563EB;strokeColor=none;fontColor=#ffffff;fontSize=12.5;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="292" y="140" width="24" height="24" as="geometry" />
        </mxCell>

        <!-- STAGE 1 CARDS -->
        <mxCell id="s1_c1" value="&lt;table width=&quot;100%&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;tr&gt;&lt;td align=&quot;center&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128444;&#65039; Load Images&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#64748B; margin-top:5px;&quot;&gt;(ImageNet / BigGAN / Defactify)&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="300" y="180" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s1_c2" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#9881;&#65039; Preprocess&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; Resize / Center Crop (128x128)&lt;br&gt;&amp;bull; JPEG Recompression (Q: 65-95)&lt;br&gt;&amp;bull; Group-Stratified Train / Val / Test Split&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="642" y="180" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s1_c3" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128452;&#65039; Organize Dataset&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; Binary Labels (Real=0, Fake=1)&lt;br&gt;&amp;bull; 6-Class Attribution Labels&lt;br&gt;&amp;bull; Leakage-Free Caption Hash Grouping&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="985" y="180" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s1_arr1" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s1_c1" target="s1_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="s1_arr2" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s1_c2" target="s1_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- DOWN ARROW 1 -> 2 -->
        <mxCell id="down1" value="" style="endArrow=classic;html=1;strokeWidth=3;strokeColor=#2563EB;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="790" y="295" as="sourcePoint" />
            <mxPoint x="790" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- ==================== STAGE 2: MODEL TRAINING & FEATURE LEARNING ==================== -->
        <mxCell id="stage2_box" value="&lt;div align=&quot;left&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif; font-size:14.5px; font-weight:700; color:#0F172A; padding-left:36px; padding-top:2px;&quot;&gt;Model Training &amp;amp; Feature Learning&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#22C55E;strokeWidth=1.8;arcSize=8;verticalAlign=top;align=left;spacingTop=8;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="280" y="320" width="1020" height="165" as="geometry" />
        </mxCell>

        <!-- BADGE 2 -->
        <mxCell id="b2" value="2" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#16A34A;strokeColor=none;fontColor=#ffffff;fontSize=12.5;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="292" y="330" width="24" height="24" as="geometry" />
        </mxCell>

        <!-- STAGE 2 CARDS -->
        <mxCell id="s2_c1" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128736;&#65039; Feature Extraction&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; ResNet-50 (2048-dim Backbone)&lt;br&gt;&amp;bull; ConvNeXt-Tiny (768-dim Modern)&lt;br&gt;&amp;bull; Frozen Head vs Full Fine-Tuning&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="300" y="370" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s2_c2" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128202; Deep Feature Fusion&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; Global Average Pooling (GAP)&lt;br&gt;&amp;bull; Multi-Scale Texture Features&lt;br&gt;&amp;bull; Cosine Annealing &amp;amp; AdamW Optim&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="642" y="370" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s2_c3" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128161; Dual-Head Learning&lt;/div&gt;&lt;table width=&quot;100%&quot; style=&quot;margin-top:3px;&quot;&gt;&lt;tr&gt;&lt;td style=&quot;font-size:11px; color:#475569; line-height:1.4;&quot;&gt;&amp;bull; Binary Classifier Head&lt;br&gt;&amp;bull; 6-Class Attribution Head&lt;br&gt;&amp;bull; Mixed Precision FP16 (AMP)&lt;/td&gt;&lt;td align=&quot;center&quot; style=&quot;font-size:26px; color:#64748B; width:14px; font-weight:300;&quot;&gt;}&lt;/td&gt;&lt;td style=&quot;font-size:10px; font-weight:700; color:#16A34A; line-height:1.2;&quot;&gt;Unified&lt;br&gt;Forensic&lt;br&gt;Embedding&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="985" y="370" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s2_arr1" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s2_c1" target="s2_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="s2_arr2" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s2_c2" target="s2_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- DOWN ARROW 2 -> 3 -->
        <mxCell id="down2" value="" style="endArrow=classic;html=1;strokeWidth=3;strokeColor=#16A34A;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="790" y="485" as="sourcePoint" />
            <mxPoint x="790" y="510" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- ==================== STAGE 3: MODEL EVALUATION & ANALYSIS ==================== -->
        <mxCell id="stage3_box" value="&lt;div align=&quot;left&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif; font-size:14.5px; font-weight:700; color:#0F172A; padding-left:36px; padding-top:2px;&quot;&gt;Model Evaluation &amp;amp; Analysis&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#A855F7;strokeWidth=1.8;arcSize=8;verticalAlign=top;align=left;spacingTop=8;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="280" y="510" width="1020" height="165" as="geometry" />
        </mxCell>

        <!-- BADGE 3 -->
        <mxCell id="b3" value="3" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#9333EA;strokeColor=none;fontColor=#ffffff;fontSize=12.5;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="292" y="520" width="24" height="24" as="geometry" />
        </mxCell>

        <!-- STAGE 3 CARDS -->
        <mxCell id="s3_c1" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128200; Cross-Generator Evaluation&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; In-Distribution Test ('seen_all')&lt;br&gt;&amp;bull; Leave-One-Generator-Out (LOGO)&lt;br&gt;&amp;bull; Unseen Generator Tests (6 Splits)&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="300" y="560" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s3_c2" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#127919; Comparative Benchmarking&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; ResNet-50 vs ConvNeXt-Tiny&lt;br&gt;&amp;bull; Precision / Recall / F1-Score&lt;br&gt;&amp;bull; AUROC &amp;amp; Precision-Recall Curves&lt;br&gt;&amp;bull; Per-Generator Accuracy Breakdown&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="642" y="560" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s3_c3" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128196; Robustness Analysis&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; GAN &amp;harr; Diffusion Transferability&lt;br&gt;&amp;bull; Post-Compression Resistance (JPEG)&lt;br&gt;&amp;bull; Generalization Gap Quantification&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="985" y="560" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s3_arr1" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s3_c1" target="s3_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="s3_arr2" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s3_c2" target="s3_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- DOWN ARROW 3 -> 4 -->
        <mxCell id="down3" value="" style="endArrow=classic;html=1;strokeWidth=3;strokeColor=#9333EA;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="790" y="675" as="sourcePoint" />
            <mxPoint x="790" y="700" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- ==================== STAGE 4: RESULTS & FORENSIC INSIGHTS ==================== -->
        <mxCell id="stage4_box" value="&lt;div align=&quot;left&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif; font-size:14.5px; font-weight:700; color:#0F172A; padding-left:36px; padding-top:2px;&quot;&gt;Results &amp;amp; Forensic Insights&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF7ED;strokeColor=#F97316;strokeWidth=1.8;arcSize=8;verticalAlign=top;align=left;spacingTop=8;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="280" y="700" width="1020" height="160" as="geometry" />
        </mxCell>

        <!-- BADGE 4 -->
        <mxCell id="b4" value="4" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#EA580C;strokeColor=none;fontColor=#ffffff;fontSize=12.5;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="292" y="710" width="24" height="24" as="geometry" />
        </mxCell>

        <!-- STAGE 4 CARDS -->
        <mxCell id="s4_c1" value="&lt;table width=&quot;100%&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;tr&gt;&lt;td align=&quot;center&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128444;&#65039; Authenticity Prediction&lt;/div&gt;&lt;div style=&quot;font-size:12px; font-weight:700; color:#EA580C; margin-top:3px;&quot;&gt;Real vs. AI-Generated&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#64748B; margin-top:3px;&quot;&gt;Confidence score &amp;amp; binary decision&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="300" y="745" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s4_c2" value="&lt;table width=&quot;100%&quot; style=&quot;font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;tr&gt;&lt;td align=&quot;center&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128269; Source Attribution&lt;/div&gt;&lt;div style=&quot;font-size:12px; font-weight:700; color:#EA580C; margin-top:3px;&quot;&gt;6-Class Generator Prediction&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#64748B; margin-top:3px;&quot;&gt;BigGAN, DALL-E, MJ, SD 2.1/3/XL&lt;/div&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="642" y="745" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s4_c3" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:13px; font-weight:700; color:#0F172A;&quot;&gt;&#128221; Evaluation Reports&lt;/div&gt;&lt;div style=&quot;font-size:11px; color:#475569; line-height:1.45; margin-top:4px;&quot;&gt;&amp;bull; AUROC, F1-Score &amp;amp; Confusion Matrix&lt;br&gt;&amp;bull; Color-Coded Prediction Visualizer&lt;br&gt;&amp;bull; Evidence-Based Digital Forensics&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;strokeWidth=1.4;arcSize=8;shadow=1;fontColor=#1E293B;" vertex="1" parent="1">
          <mxGeometry x="985" y="745" width="295" height="95" as="geometry" />
        </mxCell>

        <mxCell id="s4_arr1" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s4_c1" target="s4_c2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="s4_arr2" value="" style="endArrow=classic;html=1;strokeWidth=2;strokeColor=#94A3B8;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="s4_c2" target="s4_c3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ==================== RIGHT TOP: EXTERNAL RESOURCES ==================== -->
        <mxCell id="ext_box" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:14.5px; font-weight:700; color:#0F172A;&quot;&gt;&#9729;&#65039; External Resources&lt;/div&gt;&lt;hr style=&quot;border:none; border-top:1px solid #BAE6FD; margin:8px 0;&quot;&gt;&lt;div style=&quot;font-size:11.5px; color:#334155; line-height:1.7;&quot;&gt;&#128452;&#65039; &lt;b style=&quot;color:#0F172A;&quot;&gt;Defactify Dataset&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;Multi-Diffusion Benchmark&lt;/span&gt;&lt;br&gt;&lt;br&gt;&#128444;&#65039; &lt;b style=&quot;color:#0F172A;&quot;&gt;ImageNet-1K&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;Authentic baseline photos&lt;/span&gt;&lt;br&gt;&lt;br&gt;&#9881;&#65039; &lt;b style=&quot;color:#0F172A;&quot;&gt;GenImage BigGAN&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;GAN synthesis benchmark&lt;/span&gt;&lt;br&gt;&lt;br&gt;&#128187; &lt;b style=&quot;color:#0F172A;&quot;&gt;PyTorch / HF&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;span style=&quot;color:#64748B;&quot;&gt;Models, datasets &amp;amp; GPU AMP&lt;/span&gt;&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0F9FF;strokeColor=#0284C7;strokeWidth=1.8;arcSize=8;verticalAlign=top;spacingTop=10;spacingLeft=10;spacingRight=10;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="1320" y="130" width="280" height="355" as="geometry" />
        </mxCell>

        <!-- ARROW: EXTERNAL RESOURCES -> STAGE 1 -->
        <mxCell id="arr_ext_s1" value="" style="endArrow=classic;html=1;strokeWidth=2.5;strokeColor=#0284C7;exitX=0;exitY=0.25;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="ext_box" target="stage1_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ==================== RIGHT BOTTOM: OUTPUTS ==================== -->
        <mxCell id="out_box" value="&lt;div align=&quot;left&quot; style=&quot;padding:4px; font-family:Inter,Segoe UI,sans-serif;&quot;&gt;&lt;div style=&quot;font-size:14.5px; font-weight:700; color:#0F172A;&quot;&gt;&#128196; Outputs&lt;/div&gt;&lt;hr style=&quot;border:none; border-top:1px solid #E9D5FF; margin:8px 0;&quot;&gt;&lt;div style=&quot;font-size:11.5px; color:#334155; line-height:1.6;&quot;&gt;&#128202; &lt;b style=&quot;color:#0F172A;&quot;&gt;Predictions &amp;amp; Reports&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; Authenticity Probability&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; Source Attribution Class&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; Grid Visualizations&lt;br&gt;&lt;br&gt;&#11088; &lt;b style=&quot;color:#0F172A;&quot;&gt;Trained Models&lt;/b&gt;&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; ResNet-50 Best PT Weights&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; ConvNeXt-Tiny Checkpoints&lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;bull; 18 Benchmark Models&lt;/div&gt;&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#7C3AED;strokeWidth=1.8;arcSize=8;verticalAlign=top;spacingTop=10;spacingLeft=10;spacingRight=10;shadow=0;" vertex="1" parent="1">
          <mxGeometry x="1320" y="510" width="280" height="350" as="geometry" />
        </mxCell>

        <!-- ARROW: STAGE 4 -> OUTPUTS -->
        <mxCell id="arr_s4_out" value="" style="endArrow=classic;html=1;strokeWidth=2.5;strokeColor=#7C3AED;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.7;entryDx=0;entryDy=0;" edge="1" parent="1" source="stage4_box" target="out_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ==================== BOTTOM STATUS BAR ==================== -->
        <mxCell id="footer" value="&lt;table width=&quot;100%&quot; style=&quot;font-size:11.5px; font-family:Inter,Segoe UI,sans-serif; color:#1E293B;&quot;&gt;&lt;tr&gt;&lt;td align=&quot;center&quot; width=&quot;20%&quot;&gt;&lt;b&gt;&#128452;&#65039; Datasets&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#64748B;&quot;&gt;(ImageNet / BigGAN / Defactify)&lt;/span&gt;&lt;/td&gt;&lt;td style=&quot;border-left:1px solid #CBD5E1;&quot; align=&quot;center&quot; width=&quot;20%&quot;&gt;&lt;b&gt;&#128736;&#65039; Models&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#64748B;&quot;&gt;(ResNet-50 / ConvNeXt-Tiny)&lt;/span&gt;&lt;/td&gt;&lt;td style=&quot;border-left:1px solid #CBD5E1;&quot; align=&quot;center&quot; width=&quot;20%&quot;&gt;&lt;b&gt;&#128187; Framework&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#64748B;&quot;&gt;(PyTorch / Torchvision / AMP)&lt;/span&gt;&lt;/td&gt;&lt;td style=&quot;border-left:1px solid #CBD5E1;&quot; align=&quot;center&quot; width=&quot;20%&quot;&gt;&lt;b&gt;&#128200; Evaluation&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#64748B;&quot;&gt;(AUC / Precision / Recall / F1)&lt;/span&gt;&lt;/td&gt;&lt;td style=&quot;border-left:1px solid #CBD5E1;&quot; align=&quot;center&quot; width=&quot;20%&quot;&gt;&lt;b&gt;&#128196; Reports&lt;/b&gt;&lt;br&gt;&lt;span style=&quot;color:#64748B;&quot;&gt;(Forensic Attribution &amp;amp; Analysis)&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;arcSize=8;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="880" width="1560" height="60" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def execute():
    xml = build_drawio_xml()
    
    # Save .drawio files
    with open("CrossGen_Forensics_Architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml)
    with open("assets/CrossGen_Forensics_Architecture.drawio", "w", encoding="utf-8") as f:
        f.write(xml)
    print("Saved CrossGen_Forensics_Architecture.drawio successfully!")

    # Generate 1-click draw.io URL
    import re
    match = re.search(r'<mxGraphModel.*?</mxGraphModel>', xml, re.DOTALL)
    if match:
        model_xml = match.group(0)
        quoted = urllib.parse.quote(model_xml, safe='~()*!\'')
        deflater = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
        compressed = deflater.compress(quoted.encode('utf-8')) + deflater.flush()
        hash_val = base64.b64encode(compressed).decode('ascii')
        url = f"https://app.diagrams.net/#R{hash_val}"
        with open("drawio_link.txt", "w", encoding="utf-8") as f:
            f.write(url)
        print("Generated 1-click URL in drawio_link.txt")

    # Embed XML into PNGs
    png_path = "CrossGen_Forensics_Architecture.png"
    if os.path.exists(png_path):
        with Image.open(png_path) as im:
            img = im.copy()
        meta = PngImagePlugin.PngInfo()
        meta.add_text("mxfile", xml)
        
        # Save to main directory
        img.save("temp_embed.png", pnginfo=meta)
        os.replace("temp_embed.png", png_path)
        
        # Save to assets
        img.save("assets/figure5_system_architecture.png", pnginfo=meta)
        img.save("assets/CrossGen_Forensics_Architecture.png", pnginfo=meta)
        
        # Save to artifact dir
        dst = r"C:\Users\eshan\.gemini\antigravity\brain\37ad8a3c-aaf0-4e9f-af06-194ef09dfaf1\CrossGen_Forensics_Architecture.png"
        img.save(dst, pnginfo=meta)
        print("Embedded draw.io XML with adaptiveColors='none' into PNGs!")

if __name__ == "__main__":
    execute()
