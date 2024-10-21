https://universe.roboflow.com/data-zygje/sajam


 CUDA-version: 12020 (12020), cuDNN: 8.9.6, CUDNN_HALF=1, GPU count: 1  
 CUDNN_HALF=1 
 OpenCV version: 4.5.4
 0 : compute_capability = 750, cudnn_half = 1, GPU: Tesla T4 
net.optimized_memory = 0 
mini_batch = 1, batch = 1, time_steps = 1, train = 0 
   layer   filters  size/strd(dil)      input                output
   0 Create CUDA-stream - 0 
 Create cudnn-handle 0 
conv     32       3 x 3/ 2    416 x 416 x   3 ->  208 x 208 x  32 0.075 BF
   1 conv     64       3 x 3/ 2    208 x 208 x  32 ->  104 x 104 x  64 0.399 BF
   2 conv     32       1 x 1/ 1    104 x 104 x  64 ->  104 x 104 x  32 0.044 BF
   3 route  1 		                           ->  104 x 104 x  64 
   4 conv     32       1 x 1/ 1    104 x 104 x  64 ->  104 x 104 x  32 0.044 BF
   5 conv     32       3 x 3/ 1    104 x 104 x  32 ->  104 x 104 x  32 0.199 BF
   6 conv     32       3 x 3/ 1    104 x 104 x  32 ->  104 x 104 x  32 0.199 BF
   7 route  2 4 5 6 	                   ->  104 x 104 x 128 
   8 conv     64       1 x 1/ 1    104 x 104 x 128 ->  104 x 104 x  64 0.177 BF
   9 max                2x 2/ 2    104 x 104 x  64 ->   52 x  52 x  64 0.001 BF
  10 conv     64       1 x 1/ 1     52 x  52 x  64 ->   52 x  52 x  64 0.022 BF
  11 route  9 		                           ->   52 x  52 x  64 
  12 conv     64       1 x 1/ 1     52 x  52 x  64 ->   52 x  52 x  64 0.022 BF
  13 conv     64       3 x 3/ 1     52 x  52 x  64 ->   52 x  52 x  64 0.199 BF
  14 conv     64       3 x 3/ 1     52 x  52 x  64 ->   52 x  52 x  64 0.199 BF
  15 route  10 12 13 14 	                   ->   52 x  52 x 256 
  16 conv    128       1 x 1/ 1     52 x  52 x 256 ->   52 x  52 x 128 0.177 BF
  17 max                2x 2/ 2     52 x  52 x 128 ->   26 x  26 x 128 0.000 BF
  18 conv    128       1 x 1/ 1     26 x  26 x 128 ->   26 x  26 x 128 0.022 BF
  19 route  17 		                           ->   26 x  26 x 128 
  20 conv    128       1 x 1/ 1     26 x  26 x 128 ->   26 x  26 x 128 0.022 BF
  21 conv    128       3 x 3/ 1     26 x  26 x 128 ->   26 x  26 x 128 0.199 BF
  22 conv    128       3 x 3/ 1     26 x  26 x 128 ->   26 x  26 x 128 0.199 BF
  23 route  18 20 21 22 	                   ->   26 x  26 x 512 
  24 conv    256       1 x 1/ 1     26 x  26 x 512 ->   26 x  26 x 256 0.177 BF
  25 max                2x 2/ 2     26 x  26 x 256 ->   13 x  13 x 256 0.000 BF
  26 conv    256       1 x 1/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.022 BF
  27 route  25 		                           ->   13 x  13 x 256 
  28 conv    256       1 x 1/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.022 BF
  29 conv    256       3 x 3/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.199 BF
  30 conv    256       3 x 3/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.199 BF
  31 route  26 28 29 30 	                   ->   13 x  13 x1024 
  32 conv    512       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 512 0.177 BF
  33 conv    256       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 256 0.044 BF
  34 route  32 		                           ->   13 x  13 x 512 
  35 conv    256       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 256 0.044 BF
  36 max                5x 5/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.001 BF
  37 route  35 		                           ->   13 x  13 x 256 
  38 max                9x 9/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.004 BF
  39 route  35 		                           ->   13 x  13 x 256 
  40 max               13x13/ 1     13 x  13 x 256 ->   13 x  13 x 256 0.007 BF
  41 route  40 38 36 35 	                   ->   13 x  13 x1024 
  42 conv    256       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 256 0.089 BF
  43 route  33 42 	                           ->   13 x  13 x 512 
  44 conv    256       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 256 0.044 BF
  45 conv    128       1 x 1/ 1     13 x  13 x 256 ->   13 x  13 x 128 0.011 BF
  46 upsample                 2x    13 x  13 x 128 ->   26 x  26 x 128
  47 route  24 		                           ->   26 x  26 x 256 
  48 conv    128       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x 128 0.044 BF
  49 route  48 46 	                           ->   26 x  26 x 256 
  50 conv     64       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  64 0.022 BF
  51 route  49 		                           ->   26 x  26 x 256 
  52 conv     64       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  64 0.022 BF
  53 conv     64       3 x 3/ 1     26 x  26 x  64 ->   26 x  26 x  64 0.050 BF
  54 conv     64       3 x 3/ 1     26 x  26 x  64 ->   26 x  26 x  64 0.050 BF
  55 route  50 52 53 54 	                   ->   26 x  26 x 256 
  56 conv    128       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x 128 0.044 BF
  57 conv     64       1 x 1/ 1     26 x  26 x 128 ->   26 x  26 x  64 0.011 BF
  58 upsample                 2x    26 x  26 x  64 ->   52 x  52 x  64
  59 route  16 		                           ->   52 x  52 x 128 
  60 conv     64       1 x 1/ 1     52 x  52 x 128 ->   52 x  52 x  64 0.044 BF
  61 route  60 58 	                           ->   52 x  52 x 128 
  62 conv     32       1 x 1/ 1     52 x  52 x 128 ->   52 x  52 x  32 0.022 BF
  63 route  61 		                           ->   52 x  52 x 128 
  64 conv     32       1 x 1/ 1     52 x  52 x 128 ->   52 x  52 x  32 0.022 BF
  65 conv     32       3 x 3/ 1     52 x  52 x  32 ->   52 x  52 x  32 0.050 BF
  66 conv     32       3 x 3/ 1     52 x  52 x  32 ->   52 x  52 x  32 0.050 BF
  67 route  62 64 65 66 	                   ->   52 x  52 x 128 
  68 conv     64       1 x 1/ 1     52 x  52 x 128 ->   52 x  52 x  64 0.044 BF
  69 conv    128       3 x 3/ 2     52 x  52 x  64 ->   26 x  26 x 128 0.100 BF
  70 route  69 56 	                           ->   26 x  26 x 256 
  71 conv     64       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  64 0.022 BF
  72 route  70 		                           ->   26 x  26 x 256 
  73 conv     64       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  64 0.022 BF
  74 conv     64       3 x 3/ 1     26 x  26 x  64 ->   26 x  26 x  64 0.050 BF
  75 conv     64       3 x 3/ 1     26 x  26 x  64 ->   26 x  26 x  64 0.050 BF
  76 route  71 73 74 75 	                   ->   26 x  26 x 256 
  77 conv    128       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x 128 0.044 BF
  78 conv    256       3 x 3/ 2     26 x  26 x 128 ->   13 x  13 x 256 0.100 BF
  79 route  78 44 	                           ->   13 x  13 x 512 
  80 conv    128       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 128 0.022 BF
  81 route  79 		                           ->   13 x  13 x 512 
  82 conv    128       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 128 0.022 BF
  83 conv    128       3 x 3/ 1     13 x  13 x 128 ->   13 x  13 x 128 0.050 BF
  84 conv    128       3 x 3/ 1     13 x  13 x 128 ->   13 x  13 x 128 0.050 BF
  85 route  80 82 83 84 	                   ->   13 x  13 x 512 
  86 conv    256       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x 256 0.044 BF
  87 route  68 		                           ->   52 x  52 x  64 
  88 conv    128       3 x 3/ 1     52 x  52 x  64 ->   52 x  52 x 128 0.399 BF
  89 conv     21       1 x 1/ 1     52 x  52 x 128 ->   52 x  52 x  21 0.015 BF
  90 yolo
[yolo] params: iou loss: ciou (4), iou_norm: 0.05, obj_norm: 1.00, cls_norm: 0.50, delta_norm: 1.00, scale_x_y: 2.00
nms_kind: diounms (2), beta = 0.600000 
  91 route  77 		                           ->   26 x  26 x 128 
  92 conv    256       3 x 3/ 1     26 x  26 x 128 ->   26 x  26 x 256 0.399 BF
  93 conv     21       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  21 0.007 BF
  94 yolo
[yolo] params: iou loss: ciou (4), iou_norm: 0.05, obj_norm: 1.00, cls_norm: 0.50, delta_norm: 1.00, scale_x_y: 2.00
nms_kind: diounms (2), beta = 0.600000 
  95 route  86 		                           ->   13 x  13 x 256 
  96 conv    512       3 x 3/ 1     13 x  13 x 256 ->   13 x  13 x 512 0.399 BF
  97 conv     21       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x  21 0.004 BF
  98 yolo
[yolo] params: iou loss: ciou (4), iou_norm: 0.05, obj_norm: 1.00, cls_norm: 0.50, delta_norm: 1.00, scale_x_y: 2.00
nms_kind: diounms (2), beta = 0.600000 
Total BFLOPS 5.518 
avg_outputs = 165602 
 Allocate additional workspace_size = 13.11 MB 
Loading weights from /content/darknet/backup/yolov7-tiny_final.weights...
 seen 64, trained: 256 K-images (4 Kilo-batches_64) 
Done! Loaded 99 layers from weights-file 

 calculation mAP (mean average precision)...
 Detection layer: 90 - type = 28 
 Detection layer: 94 - type = 28 
 Detection layer: 98 - type = 28 
92
 detections_count = 2401, unique_truth_count = 92  
class_id = 0, name = celurit, ap = 7.99%   	 (TP = 0, FP = 0) 
class_id = 1, name = pedang, ap = 9.57%   	 (TP = 0, FP = 0) 

 for conf_thresh = 0.25, precision = -nan, recall = 0.00, F1-score = -nan 
 for conf_thresh = 0.25, TP = 0, FP = 0, FN = 92, average IoU = 0.00 % 

 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall 
 mean average precision (mAP@0.50) = 0.087778, or 8.78 % 
Total Detection Time: 2 Seconds

Set -points flag:
 `-points 101` for MS COCO 
 `-points 11` for PascalVOC 2007 (uncomment `difficult` in voc.data) 
 `-points 0` (AUC) for ImageNet, PascalVOC 2010-2012, your custom dataset
