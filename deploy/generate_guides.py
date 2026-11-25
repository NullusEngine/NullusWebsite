#!/usr/bin/env python3
"""Generate the bilingual, static guides served by the official website."""

import argparse
import html
import json
from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.nullusengine.com"
GITHUB = "https://github.com/NullusEngine/Nullus/blob/main/Docs"

GUIDES = {
    "rendering": {
        "zh-cn": {
            "lang": "zh-CN",
            "title": "实时渲染与多后端 RHI | Nullus Engine",
            "description": "了解 Nullus 的实时 3D 渲染架构：FrameGraph、显式 RHI、HLSL、前向与延迟渲染，以及 DX12、Vulkan 和 Metal 的平台状态。",
            "eyebrow": "RENDERING / FRAMEGRAPH / RHI",
            "heading": "实时 3D 渲染，从场景到 GPU",
            "lead": "Nullus 将场景更新、FrameGraph 和显式 RHI 串成一条可追踪的渲染路径，让 Editor 与 Player 使用同一套渲染主线。",
            "breadcrumb": "实时渲染",
            "nav_home": "首页",
            "nav_rendering": "渲染架构",
            "nav_start": "快速开始",
            "language_label": "Switch to English",
            "language_text": "EN",
            "on_page": "本页内容",
            "links": [("frame", "一帧的路径"), ("framegraph", "FrameGraph 与渲染路径"), ("shaders", "HLSL 与材质"), ("platforms", "平台与验证范围")],
            "sections": """
              <section class="guide-section" id="frame">
                <h2>一帧如何从场景到屏幕</h2>
                <p>Game Thread 通过命令更新场景渲染数据，Render Thread 构建帧，RHI 通道负责翻译和提交原生命令。场景数据由 <code>SceneRenderStore</code> 持有，每帧载荷包含相机、视图和输出目标等参数。</p>
                <div class="guide-flow" aria-label="渲染流程"><span>Game Thread</span><span aria-hidden="true">→</span><span>Render Thread</span><span aria-hidden="true">→</span><span>RHI Submit</span></div>
                <p>渲染工作可使用 TaskGraph 的执行通道。帧资源复用由 GPU 围栏控制，便于在性能分析和扩展时区分线程、资源与提交的职责。</p>
              </section>
              <section class="guide-section" id="framegraph">
                <h2>FrameGraph 管理渲染 Pass</h2>
                <p>FrameGraph 描述各 Pass 的输入、输出和资源状态，管理 Pass 依赖与资源状态转换。Nullus 的前向和延迟渲染路径共享这套资源管理方式。</p>
                <ul><li><strong>Forward</strong> 包含深度预通道、前向着色、透明物体、天空盒和编辑器叠加层。</li><li><strong>Deferred</strong> 包含 GBuffer、clustered lighting、decal、延迟光照和透明输出。</li><li><strong>大场景基础</strong> 包含可见性收集、绘制命令缓存、实例化合批和静态网格 LOD。</li></ul>
              </section>
              <section class="guide-section" id="shaders">
                <h2>HLSL、ShaderLab 与 PBR 材质</h2>
                <p>HLSL 是引擎维护的着色器源，编译过程生成 DXIL、SPIR-V 和反射数据。ShaderLab 描述材质属性和渲染状态，内置 StandardPBR 提供模型导入使用的材质基线。</p>
                <p>Material Editor 支持编辑材质参数、ShaderLab 和 ShaderGraph，并提供预览。模型导入可生成网格、材质、纹理和 Prefab 子资源。</p>
              </section>
              <section class="guide-section" id="platforms">
                <h2>图形后端与平台状态</h2>
                <p>Windows 使用 DX12，Linux 与 WSL 使用 Vulkan 1.1，均为当前运行主线。macOS 提供 Metal 构建目标与原生后端，设备运行验证需要单独进行。DX12 的 HZB 遮挡剔除按设备能力启用。</p>
                <p>具体功能的可用性与验证范围请查看 <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/zh-CN/rendering/backends.md">图形后端与大场景特性</a> 和 <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/zh-CN/platform-build/platforms.md">平台支持矩阵</a>。</p>
              </section>
            """,
            "next_label": "准备开始构建？",
            "next_text": "查看环境要求、平台构建命令和第一个项目的步骤。",
            "next_link": "阅读快速开始",
            "next_route": "getting-started",
            "source_label": "阅读渲染手册",
            "source_path": "zh-CN/rendering/overview.md",
            "footer": "面向实时 3D 创作的 C++20 原生引擎。",
        },
        "en": {
            "lang": "en",
            "title": "Real-Time Rendering and RHI | Nullus Engine",
            "description": "Explore the Nullus real-time 3D rendering architecture: FrameGraph, explicit RHI, HLSL, forward and deferred paths, and DX12, Vulkan, and Metal platform status.",
            "eyebrow": "RENDERING / FRAMEGRAPH / RHI",
            "heading": "Real-time 3D rendering from scene to GPU",
            "lead": "Nullus connects scene updates, FrameGraph, and an explicit RHI in a traceable rendering pipeline shared by the Editor and Player.",
            "breadcrumb": "Real-time rendering",
            "nav_home": "Home",
            "nav_rendering": "Rendering",
            "nav_start": "Get started",
            "language_label": "切换为中文",
            "language_text": "中",
            "on_page": "On this page",
            "links": [("frame", "The path of a frame"), ("framegraph", "FrameGraph and render paths"), ("shaders", "HLSL and materials"), ("platforms", "Platform status")],
            "sections": """
              <section class="guide-section" id="frame">
                <h2>The path from scene to screen</h2>
                <p>The Game Thread updates scene rendering data through commands, the Render Thread builds the frame, and the RHI lane translates and submits native commands. <code>SceneRenderStore</code> holds persistent rendering data, while each frame carries camera, view, and output parameters.</p>
                <div class="guide-flow" aria-label="Rendering pipeline"><span>Game Thread</span><span aria-hidden="true">→</span><span>Render Thread</span><span aria-hidden="true">→</span><span>RHI Submit</span></div>
                <p>Rendering work uses TaskGraph execution lanes. GPU fences control frame-resource reuse, keeping thread, resource, and submission responsibilities clear when profiling or extending the engine.</p>
              </section>
              <section class="guide-section" id="framegraph">
                <h2>FrameGraph manages rendering passes</h2>
                <p>FrameGraph describes each pass's inputs, outputs, and resource states, then manages pass dependencies and resource transitions. Both the forward and deferred paths share this resource management model.</p>
                <ul><li><strong>Forward</strong> includes a depth prepass, forward shading, transparent objects, skybox, and editor overlays.</li><li><strong>Deferred</strong> includes the GBuffer, clustered lighting, decals, deferred lighting, and transparent output.</li><li><strong>Large-scene foundations</strong> include visibility collection, draw-command caching, instancing, and static-mesh LOD.</li></ul>
              </section>
              <section class="guide-section" id="shaders">
                <h2>HLSL, ShaderLab, and PBR materials</h2>
                <p>HLSL is the engine's maintained shader source. Compilation produces DXIL, SPIR-V, and reflection data. ShaderLab describes material properties and rendering state, while the built-in StandardPBR provides a baseline for imported models.</p>
                <p>The Material Editor supports material parameters, ShaderLab, and ShaderGraph with previews. Model import can produce meshes, materials, textures, and Prefab sub-assets.</p>
              </section>
              <section class="guide-section" id="platforms">
                <h2>Graphics backends and platform status</h2>
                <p>Windows uses DX12 and Linux or WSL uses Vulkan 1.1, both current runtime mainlines. macOS has a Metal build target and native backend, with device runtime validation tracked separately. DX12 HZB occlusion is enabled according to device capabilities.</p>
                <p>For feature availability and validation scope, see <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/en/rendering/backends.md">graphics backends and large scenes</a> and the <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/en/platform-build/platforms.md">platform matrix</a>.</p>
              </section>
            """,
            "next_label": "Ready to build?",
            "next_text": "See the requirements, platform build commands, and steps for a first project.",
            "next_link": "Read the quick start",
            "next_route": "getting-started",
            "source_label": "Read the rendering handbook",
            "source_path": "en/rendering/overview.md",
            "footer": "A native C++20 engine for real-time 3D creation.",
        },
    },
    "getting-started": {
        "zh-cn": {
            "lang": "zh-CN",
            "title": "从源码构建与创建第一个项目 | Nullus Engine",
            "description": "了解 Nullus 游戏引擎的环境要求、Windows、Linux 和 macOS 构建命令，以及如何在 Editor 中创建第一个场景。",
            "eyebrow": "GET STARTED / BUILD / EDITOR",
            "heading": "构建 Nullus，创建第一个项目",
            "lead": "从源码准备 C++20 工具链，构建 Editor 与 Launcher，然后在编辑器中创建场景并运行脚本。",
            "breadcrumb": "快速开始",
            "nav_home": "首页",
            "nav_rendering": "渲染架构",
            "nav_start": "快速开始",
            "language_label": "Switch to English",
            "language_text": "EN",
            "on_page": "本页内容",
            "links": [("requirements", "环境要求"), ("build", "获取源码与构建"), ("first-project", "创建第一个项目"), ("license", "许可与下一步")],
            "sections": """
              <section class="guide-section" id="requirements">
                <h2>构建前需要什么</h2>
                <p>准备 Git、CMake 3.22 或更高版本、支持 C++20 的编译器和 Python 3.8 或更高版本。.NET SDK 由仓库中的 <code>global.json</code> 固定为 8.0.408，缺失时 CMake 会准备仓库内副本。</p>
                <ul><li><strong>Windows</strong> 使用 Visual Studio 2022 的 MSVC 工具链和 DX12。</li><li><strong>Linux / WSL</strong> 使用 GCC 或 Clang 与 Vulkan，所需 Vulkan SDK 版本见构建手册。</li><li><strong>macOS</strong> 使用 Xcode 工具链与 Metal，运行时设备验证单独记录。</li></ul>
              </section>
              <section class="guide-section" id="build">
                <h2>获取源码并构建</h2>
                <p>先克隆仓库，然后按操作系统执行对应的依赖准备与构建命令。首次配置可能需要下载第三方依赖。</p>
                <pre><code>git clone https://github.com/NullusEngine/Nullus.git
cd Nullus</code></pre>
                <h3>Windows · PowerShell</h3>
                <pre><code>.\\SetupDependencies.bat
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Debug --target Editor Launcher</code></pre>
                <h3>Linux</h3>
                <pre><code>./SetupDependencies.sh
./build_linux.sh debug</code></pre>
                <h3>macOS</h3>
                <pre><code>./SetupDependencies.sh
NLS_BUILD_TARGETS="Editor Launcher" ./build_macos.sh debug</code></pre>
                <p>构建输出位置、依赖版本与常见错误处理见<a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/zh-CN/getting-started/build.md">环境准备与构建手册</a>。</p>
              </section>
              <section class="guide-section" id="first-project">
                <h2>在 Editor 中创建第一个场景</h2>
                <ol><li>启动 Launcher，选择项目名称、路径和模板，然后打开项目。</li><li>新建场景，在 Hierarchy 中创建对象，用 Inspector 编辑组件和 Transform。</li><li>保存场景，在 Asset Browser 中创建 C# 或 Lua 脚本并挂到对象上。</li><li>按 Play，在 Game View 查看运行结果，用 Console 检查脚本日志。</li></ol>
                <p>手册中的<a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/zh-CN/getting-started/first-project.md">第一个项目</a>提供相机、立方体和旋转脚本的完整步骤。</p>
              </section>
              <section class="guide-section" id="license">
                <h2>许可与下一步</h2>
                <p>Nullus 使用自定义 Source-Available License，允许按许可条款制作和发行商业或非商业游戏。使用和贡献源码前，请阅读<a href="https://github.com/NullusEngine/Nullus/blob/main/LICENSE">完整许可证</a>及贡献条款。</p>
                <p>需要了解渲染后端与平台边界时，可继续阅读<a href="../rendering/" data-file-href="../rendering/index.html">实时渲染架构</a>。</p>
              </section>
            """,
            "next_label": "继续探索渲染架构",
            "next_text": "了解 FrameGraph、渲染线程、着色器与图形后端。",
            "next_link": "阅读渲染介绍",
            "next_route": "rendering",
            "source_label": "阅读完整构建手册",
            "source_path": "zh-CN/getting-started/build.md",
            "footer": "面向实时 3D 创作的 C++20 原生引擎。",
        },
        "en": {
            "lang": "en",
            "title": "Build from Source and Create a Project | Nullus Engine",
            "description": "Find Nullus game engine requirements, build commands for Windows, Linux, and macOS, and the steps to create a first scene in the Editor.",
            "eyebrow": "GET STARTED / BUILD / EDITOR",
            "heading": "Build Nullus and create your first project",
            "lead": "Prepare a C++20 toolchain, build the Editor and Launcher from source, then create a scene and run a script.",
            "breadcrumb": "Getting started",
            "nav_home": "Home",
            "nav_rendering": "Rendering",
            "nav_start": "Get started",
            "language_label": "切换为中文",
            "language_text": "中",
            "on_page": "On this page",
            "links": [("requirements", "Requirements"), ("build", "Get the source and build"), ("first-project", "Create a first project"), ("license", "License and next steps")],
            "sections": """
              <section class="guide-section" id="requirements">
                <h2>What you need to build</h2>
                <p>Install Git, CMake 3.22 or newer, a C++20 compiler, and Python 3.8 or newer. The repository's <code>global.json</code> pins .NET SDK 8.0.408. CMake prepares a repository-local copy if it is missing.</p>
                <ul><li><strong>Windows</strong> uses the Visual Studio 2022 MSVC toolchain and DX12.</li><li><strong>Linux / WSL</strong> uses GCC or Clang and Vulkan. Check the build handbook for the Vulkan SDK version.</li><li><strong>macOS</strong> uses Xcode and Metal. Runtime validation on devices is tracked separately.</li></ul>
              </section>
              <section class="guide-section" id="build">
                <h2>Get the source and build</h2>
                <p>Clone the repository, then run the dependency preparation and build commands for your operating system. The first configuration may download third-party dependencies.</p>
                <pre><code>git clone https://github.com/NullusEngine/Nullus.git
cd Nullus</code></pre>
                <h3>Windows · PowerShell</h3>
                <pre><code>.\\SetupDependencies.bat
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Debug --target Editor Launcher</code></pre>
                <h3>Linux</h3>
                <pre><code>./SetupDependencies.sh
./build_linux.sh debug</code></pre>
                <h3>macOS</h3>
                <pre><code>./SetupDependencies.sh
NLS_BUILD_TARGETS="Editor Launcher" ./build_macos.sh debug</code></pre>
                <p>See the <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/en/getting-started/build.md">environment and build handbook</a> for output paths, dependency versions, and troubleshooting.</p>
              </section>
              <section class="guide-section" id="first-project">
                <h2>Create your first scene in the Editor</h2>
                <ol><li>Start the Launcher, choose a project name, location, and template, then open the project.</li><li>Create a scene and objects in the Hierarchy. Edit components and transforms in the Inspector.</li><li>Save the scene. Create a C# or Lua script in the Asset Browser and attach it to an object.</li><li>Press Play, inspect the result in Game View, and check script output in the Console.</li></ol>
                <p>The <a href="https://github.com/NullusEngine/Nullus/blob/main/Docs/en/getting-started/first-project.md">first project guide</a> includes complete steps for a camera, cube, and rotating script.</p>
              </section>
              <section class="guide-section" id="license">
                <h2>License and next steps</h2>
                <p>Nullus uses a custom Source-Available License that allows commercial and non-commercial games under its terms. Read the <a href="https://github.com/NullusEngine/Nullus/blob/main/LICENSE">full license</a> and contribution terms before using or contributing source code.</p>
                <p>Continue with the <a href="../rendering/" data-file-href="../rendering/index.html">rendering architecture</a> for backend and platform details.</p>
              </section>
            """,
            "next_label": "Explore the rendering architecture",
            "next_text": "Learn about FrameGraph, rendering threads, shaders, and graphics backends.",
            "next_link": "Read about rendering",
            "next_route": "rendering",
            "source_label": "Read the full build handbook",
            "source_path": "en/getting-started/build.md",
            "footer": "A native C++20 engine for real-time 3D creation.",
        },
    },
}


def render_guide(route, locale, data):
    other_locale = "en" if locale == "zh-cn" else "zh-cn"
    canonical = f"{ORIGIN}/{locale}/{route}/"
    alternate_zh = f"{ORIGIN}/zh-cn/{route}/"
    alternate_en = f"{ORIGIN}/en/{route}/"
    locale_og, locale_alternate = ("zh_CN", "en_US") if locale == "zh-cn" else ("en_US", "zh_CN")
    metadata = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": f"{canonical}#webpage", "url": canonical,
             "name": data["title"], "description": data["description"], "inLanguage": data["lang"],
             "isPartOf": {"@id": f"{ORIGIN}/#website"}, "breadcrumb": {"@id": f"{canonical}#breadcrumb"}},
            {"@type": "BreadcrumbList", "@id": f"{canonical}#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Nullus Engine", "item": f"{ORIGIN}/{locale}/"},
                {"@type": "ListItem", "position": 2, "name": data["breadcrumb"], "item": canonical},
            ]},
        ],
    }
    esc = lambda value: html.escape(value, quote=True)
    toc = "\n".join(f'<a href="#{esc(anchor)}">{esc(label)}</a>' for anchor, label in data["links"])
    sections = textwrap.dedent(data["sections"]).strip()
    json_ld = json.dumps(metadata, ensure_ascii=False, indent=2)
    return f'''<!doctype html>
<!-- Generated by deploy/generate_guides.py. Edit the source and regenerate. -->
<html lang="{esc(data["lang"])}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#070b12">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <title>{esc(data["title"])}</title>
  <meta name="description" content="{esc(data["description"])}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="zh-CN" href="{alternate_zh}">
  <link rel="alternate" hreflang="en" href="{alternate_en}">
  <link rel="alternate" hreflang="x-default" href="{alternate_zh}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Nullus Engine">
  <meta property="og:locale" content="{locale_og}">
  <meta property="og:locale:alternate" content="{locale_alternate}">
  <meta property="og:title" content="{esc(data["title"])}">
  <meta property="og:description" content="{esc(data["description"])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{ORIGIN}/assets/og-cover.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{'Nullus Engine 编辑器和实时 3D 场景' if locale == 'zh-cn' else 'Nullus Engine Editor and real-time 3D scene'}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(data["title"])}">
  <meta name="twitter:description" content="{esc(data["description"])}">
  <meta name="twitter:image" content="{ORIGIN}/assets/og-cover.jpg">
  <link rel="icon" href="../../assets/favicon.png" type="image/png" sizes="96x96">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../styles.css">
  <script type="application/ld+json">{json_ld}</script>
</head>
<body class="guide-page">
  <a class="skip-link" href="#main">{"跳转到主要内容" if locale == "zh-cn" else "Skip to main content"}</a>
  <header class="guide-header">
    <div class="container guide-header-inner">
      <a class="brand" href="../" data-file-href="../index.html" aria-label="Nullus Engine">
        <span class="brand-mark-wrap" aria-hidden="true"><img class="brand-mark" src="../../assets/NullusIcon.svg" alt="" width="44" height="44"></span>
        <span class="brand-copy"><span class="brand-name">NULLUS</span><span class="brand-type">ENGINE</span></span>
      </a>
      <nav class="guide-nav" aria-label="{"主导航" if locale == "zh-cn" else "Main navigation"}">
        <a href="../" data-file-href="../index.html">{esc(data["nav_home"])}</a>
        <a href="../rendering/" data-file-href="../rendering/index.html">{esc(data["nav_rendering"])}</a>
        <a href="../getting-started/" data-file-href="../getting-started/index.html">{esc(data["nav_start"])}</a>
        <a class="lang-toggle" href="../../{other_locale}/{route}/" data-file-href="../../{other_locale}/{route}/index.html" hreflang="{"en" if locale == "zh-cn" else "zh-CN"}" aria-label="{esc(data["language_label"])}">{esc(data["language_text"])}</a>
      </nav>
    </div>
  </header>
  <main id="main" class="container">
    <div class="guide-hero">
      <nav class="guide-breadcrumb" aria-label="{"面包屑导航" if locale == "zh-cn" else "Breadcrumb"}"><a href="../" data-file-href="../index.html">Nullus Engine</a><span aria-hidden="true">/</span><span aria-current="page">{esc(data["breadcrumb"])}</span></nav>
      <p class="eyebrow"><span class="eyebrow-dot"></span><span>{esc(data["eyebrow"])}</span></p>
      <h1>{esc(data["heading"])}</h1>
      <p class="guide-lead">{esc(data["lead"])}</p>
    </div>
    <div class="guide-layout">
      <article class="guide-article">
        {sections}
        <div class="guide-next"><h2>{esc(data["next_label"])}</h2><p>{esc(data["next_text"])}</p><a class="button button-primary" href="../{esc(data["next_route"])}/" data-file-href="../{esc(data["next_route"])}/index.html">{esc(data["next_link"])} <span aria-hidden="true">↗</span></a></div>
      </article>
      <aside class="guide-aside" aria-label="{esc(data["on_page"])}">
        <span class="guide-aside-label">{esc(data["on_page"])}</span>
        <nav>{toc}</nav>
        <a class="guide-source" href="{GITHUB}/{esc(data["source_path"])}" target="_blank" rel="noreferrer">{esc(data["source_label"])} <span aria-hidden="true">↗</span></a>
      </aside>
    </div>
  </main>
  <footer class="guide-footer"><div class="container guide-footer-inner"><span>© Nullus Engine</span><span>{esc(data["footer"])}</span><a href="https://github.com/NullusEngine/Nullus" target="_blank" rel="noreferrer">GitHub ↗</a></div></footer>
  <script>if (location.protocol === 'file:') document.querySelectorAll('[data-file-href]').forEach(function (link) {{ link.href = link.dataset.fileHref; }});</script>
</body>
</html>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify generated pages are up to date")
    args = parser.parse_args()
    outdated = []
    for route, locales in GUIDES.items():
        for locale, data in locales.items():
            path = ROOT / locale / route / "index.html"
            content = render_guide(route, locale, data)
            if args.check:
                if not path.is_file() or path.read_text(encoding="utf-8") != content:
                    outdated.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    if outdated:
        parser.exit(1, "Outdated guide pages: " + ", ".join(outdated) + "\n")
    print("Bilingual guides are up to date." if args.check else "Generated bilingual guides.")


if __name__ == "__main__":
    main()
