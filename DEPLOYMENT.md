# 悠悠18岁生日纪念网站 - 部署指南 🚀

## 📁 项目文件清单

### 必需的文件结构：
```
youyou-birthday-website/
├── index.html              # 主页（17张照片轮播）
├── letter.html             # 生日信页面  
├── video.html              # 视频播放页面
├── css/
│   └── style.css           # 统一样式文件
├── js/
│   └── main.js            # 交互功能脚本
├── README.md              # 项目说明文档
├── DEPLOYMENT.md          # 部署指南（本文件）
└── .gitattributes         # Git大文件管理配置
```

## 🎬 400MB视频文件处理方案

GitHub有单文件100MB的限制，400MB视频需要特殊处理：

### 方案一：Git LFS（推荐）
```bash
# 1. 安装Git LFS
git lfs install

# 2. 跟踪视频文件
git lfs track "*.mp4"
git lfs track "*.mov"
git lfs track "*.avi"

# 3. 提交.gitattributes文件
git add .gitattributes
git commit -m "Track video files with Git LFS"

# 4. 添加视频文件
git add your-video-file.mp4
git commit -m "Add birthday video"
git push origin main
```

### 方案二：云存储CDN（最佳性能）
将视频上传到以下任一云服务：

1. **阿里云OSS**
   - 上传视频到OSS存储桶
   - 设置公共读权限
   - 获取CDN加速链接

2. **腾讯云COS**
   - 上传到COS存储桶
   - 开启CDN加速
   - 获取访问链接

3. **七牛云**
   - 上传到七牛云存储
   - 获取外链地址

4. **GitHub Releases**
   - 创建新的Release
   - 上传视频文件作为附件
   - 获取下载链接

然后修改 `video.html` 中的视频源：
```html
<video class="video-player" id="videoPlayer" controls playsinline webkit-playsinline>
    <source src="YOUR_CDN_VIDEO_URL" type="video/mp4">
</video>
```

## 🌐 GitHub Pages 部署步骤

### 1. 创建GitHub仓库
```bash
# 初始化仓库
git init
git add .
git commit -m "Initial commit: 悠悠18岁生日纪念网站"

# 添加远程仓库（替换为您的用户名）
git remote add origin https://github.com/YOUR_USERNAME/youyou-birthday-website.git
git branch -M main
git push -u origin main
```

### 2. 启用GitHub Pages
1. 进入GitHub仓库设置页面
2. 滚动到 "Pages" 部分
3. 选择 "Deploy from a branch"
4. 选择 "main" 分支
5. 选择 "/ (root)" 文件夹
6. 点击 "Save"

### 3. 访问网站
部署完成后，网站将在以下地址可访问：
```
https://YOUR_USERNAME.github.io/youyou-birthday-website/
```

## 📝 配置文件

### .gitattributes
```
# Git LFS配置
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs merge=lfs -text
*.avi filter=lfs diff=lfs merge=lfs -text
*.mkv filter=lfs diff=lfs merge=lfs -text
```

### .gitignore
```
# 临时文件
.DS_Store
Thumbs.db
*.tmp
*.temp

# 备份文件
*.backup
original_letter.html
updated_letter.html

# IDE文件
.vscode/
.idea/
```

## 🔧 视频优化建议

为了更好的用户体验，建议优化视频：

### 1. 压缩视频
使用FFmpeg压缩视频：
```bash
# 压缩到合适大小（保持质量）
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4

# 进一步压缩（如果需要）
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 96k output_compressed.mp4
```

### 2. 创建多个分辨率版本
```bash
# 1080p版本
ffmpeg -i input.mp4 -vf scale=1920:1080 -c:v libx264 -crf 23 output_1080p.mp4

# 720p版本（更小文件）
ffmpeg -i input.mp4 -vf scale=1280:720 -c:v libx264 -crf 25 output_720p.mp4

# 480p版本（移动端）
ffmpeg -i input.mp4 -vf scale=854:480 -c:v libx264 -crf 27 output_480p.mp4
```

## 🌍 自定义域名配置（可选）

如果您有自己的域名：

### 1. 添加CNAME文件
在根目录创建 `CNAME` 文件：
```
youyou-birthday.yourdomain.com
```

### 2. 配置DNS
在您的域名提供商处添加CNAME记录：
```
youyou-birthday -> YOUR_USERNAME.github.io
```

## 📱 移动端优化

网站已完全适配移动端，包括：
- ✅ 响应式图片轮播
- ✅ 触摸滑动支持
- ✅ 移动端优化的导航
- ✅ 自适应视频播放器

## 🔒 隐私设置

如果需要私密访问：

### 1. 私有仓库
- 将GitHub仓库设置为Private
- 使用GitHub Pro账户启用私有仓库的Pages

### 2. 密码保护
可以添加简单的JavaScript密码保护：
```javascript
// 添加到index.html的<script>标签中
const password = "youyou2024";
const userInput = prompt("请输入访问密码：");
if (userInput !== password) {
    document.body.innerHTML = "<h1>访问被拒绝</h1>";
}
```

## 🚨 重要提醒

1. **备份文件**：部署前请备份所有文件
2. **测试链接**：确保所有照片链接正常访问
3. **视频格式**：确保视频格式兼容所有浏览器
4. **移动端测试**：在手机上测试所有功能
5. **加载速度**：监控网站加载速度，必要时优化图片

## 📞 技术支持

如遇到部署问题：
1. 检查GitHub Pages设置
2. 确认文件路径正确
3. 验证所有资源链接有效
4. 查看浏览器控制台错误信息

---

**祝愿悠悠18岁生日快乐！** 🎂✨

这个温馨的生日纪念网站将成为她人生中最珍贵的礼物之一！