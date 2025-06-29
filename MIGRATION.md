# Migration Guide: 2019 to Modern Versions

## Overview
This guide helps migrate the Medilab-plus project from 2019 dependencies to modern versions.

## Option 1: Use 2019 Compatible Versions (Recommended for Quick Setup)
```bash
pip install -r requirements-2019.txt
```
**Pros:** No code changes needed, works immediately
**Cons:** Uses older, potentially vulnerable packages

## Option 2: Upgrade to Modern Versions (Recommended for Production)
```bash
pip install -r requirements-modern.txt
```
**Requires code changes listed below.**

## Required Code Changes for Modern Versions

### 1. Update Keras Imports
Replace all `from keras` imports with `from tensorflow.keras`:

**Before:**
```python
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras import optimizers, callbacks
```

**After:**
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import optimizers, callbacks
```

### 2. Update Layer Names and Parameters
- `Convolution2D` → `Conv2D`
- `border_mode="same"` → `padding="same"`
- Remove `dim_ordering='th'` parameter

### 3. Update Training API
- `fit_generator()` → `fit()`
- `samples_per_epoch` → `steps_per_epoch`

### 4. Update Werkzeug Import
**Before:**
```python
from werkzeug import secure_filename
```

**After:**
```python
from werkzeug.utils import secure_filename
```

## Security Considerations
- 2019 versions may have known vulnerabilities
- Modern versions include security patches
- Consider using virtual environments for isolation

## Performance Benefits of Modern Versions
- Better GPU utilization with TensorFlow 2.x
- Improved memory management
- Faster training and inference
- Better debugging tools

## Recommendation
For learning/development: Use 2019 versions
For production deployment: Migrate to modern versions with code updates
