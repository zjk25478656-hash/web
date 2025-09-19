#!/bin/bash

# 悠悠18岁生日纪念网站 - 快速部署脚本
echo "🎂 开始部署悠悠的生日纪念网站..."

# 检查Git是否初始化
if [ ! -d ".git" ]; then
    echo "📋 初始化Git仓库..."
    git init
fi

# 检查是否有远程仓库
if ! git remote | grep -q origin; then
    echo "⚠️  请先设置远程仓库："
    echo "git remote add origin https://github.com/YOUR_USERNAME/youyou-birthday-website.git"
    exit 1
fi

# 添加所有文件
echo "📁 添加文件到暂存区..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Deploy: 悠悠18岁生日纪念网站 $(date '+%Y-%m-%d %H:%M:%S')"

# 推送到GitHub
echo "🚀 推送到GitHub..."
git push origin main

# 检查部署状态
echo "✅ 部署完成！"
echo ""
echo "🌐 网站将在几分钟后可访问："
echo "https://YOUR_USERNAME.github.io/youyou-birthday-website/"
echo ""
echo "🎉 悠悠的生日纪念网站已成功部署！"