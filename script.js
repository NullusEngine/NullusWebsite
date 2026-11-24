const translations = {
  zh: {
    metaTitle: 'Nullus Engine｜C++20 原生实时 3D 游戏引擎',
    metaDescription: 'Nullus 是面向实时 3D 创作的 C++20 原生游戏引擎，提供 Editor、FrameGraph、DX12、Vulkan、Metal、C#、Lua、资产管线与桌面 Player 构建。',
    navFeatures: '能力',
    navWorkflow: '工作流',
    navGallery: '展示',
    navDocs: '文档',
    navPlatforms: '平台',
    heroEyebrow: 'SOURCE AVAILABLE · REAL-TIME 3D',
    heroTitle: '用一条原生主链路，构建实时 3D 世界',
    heroLede: 'Nullus 是面向实时 3D 创作的 C++20 原生引擎。从场景、资产和脚本，到 Editor、运行时与多后端渲染，始终围绕同一套工作流。',
    heroPrimary: '开始构建',
    heroSecondary: '探索能力',
    scrollHint: '向下探索',
    proofReady: 'READY TO COMPILE',
    advantagesEyebrow: 'WHY NULLUS',
    advantagesTitle: '每一层都能追踪，每一次扩展都有位置',
    advantagesLede: 'Nullus 把创作工具、运行时和底层系统放进同一条主线。你可以从 Editor 开始，也可以直接深入渲染、资产或脚本边界。',
    metricRuntime: 'ONE CONTENT PATH',
    metricThreads: 'RENDER CHANNELS',
    metricScripts: 'SCRIPT BACKENDS',
    metricCpp: 'C++ STANDARD',
    signalRuntimeTitle: '同一套运行时，贯穿 Editor 到 Player',
    signalRuntimeText: '场景、资产和脚本在 Editor 中编辑，在 Game 中运行，再由 Build Profile 进入桌面 Player。内容不需要换一套表达方式。',
    signalRhiTitle: '显式 RHI，把性能路径摊开给你看',
    signalRhiText: 'Game Thread、Render Thread 与 RHI Submit 各自负责明确的一段工作，FrameGraph 管理 pass、资源状态和依赖。',
    signalContentTitle: '源文件到可用资产，路径清晰可复查',
    signalContentText: 'glTF、FBX、OBJ、PBR 材质、Prefab 和场景序列化都进入项目资产数据库，导入结果拥有稳定的资源身份。',
    signalScriptTitle: 'C# 与 Lua，共享对象模型和生命周期',
    signalScriptText: '两种语言连接同一套 GameObject、Component、输入与时间系统。C# 增量构建后热重载，Lua 保存后直接重载。',
    featuresEyebrow: 'ENGINE SURFACE',
    featuresTitle: '为真正的创作流程而设计',
    featuresLede: '从第一块几何体到最终 Player，每一层都连接到清晰、可观察、可扩展的引擎主线。',
    featureRenderTitle: '显式多后端渲染',
    featureRenderText: 'FrameGraph、HLSL 和统一 RHI 让 DX12、Vulkan 与 Metal 共享同一套渲染语言。',
    featureEditorTitle: 'Editor 内完成创作',
    featureEditorText: 'Hierarchy、Scene View、Inspector、播放控制和 Asset Browser 组成日常编辑闭环。',
    featureAssetsTitle: '资产直接进入场景',
    featureAssetsText: '模型、材质、纹理、Prefab 与场景序列化都连接到项目级资产数据库。',
    featureScriptTitle: 'C# 与 Lua 并行可用',
    featureScriptText: '共享原生脚本 ABI、组件生命周期和输入时间系统，在 Editor 内持续迭代。',
    featureSimTitle: '让世界开始运动',
    featureSimText: '物理、角色控制、动画和粒子工作流共享场景与运行时边界。',
    featureBuildTitle: '从项目到桌面 Player',
    featureBuildText: 'Build Profile 收集依赖、Cook 内容并组装可运行的桌面 Player。',
    learnMore: '查看详情',
    docsEyebrow: 'DEVELOPER PATH',
    docsTitle: '从第一条命令到引擎内部',
    docsLede: '官网负责告诉你 Nullus 能做什么，手册负责带你把它跑起来。选择一条入口，继续深入真实的项目文件与工作流。',
    docsBuildTitle: '环境准备与构建',
    docsBuildText: '从依赖准备、CMake 配置到 Editor、Launcher 和 Player 构建，按平台选择正确入口。',
    docsBuildMeta: 'Windows · Linux · macOS',
    docsEditorTitle: '使用 Editor',
    docsEditorText: '认识 Scene View、Game View、Hierarchy、Inspector、Asset Browser 和日常快捷键。',
    docsEditorMeta: 'Scene · Assets · Settings',
    docsArchitectureTitle: '理解引擎结构',
    docsArchitectureText: '从模块、反射与序列化，到任务系统、编辑器扩展和插件边界，沿源码继续阅读。',
    docsArchitectureMeta: 'Runtime · Editor · Modules',
    docsRead: '阅读手册',
    docsFoot: 'Docs/ 是手册源文件，中文与 English 页面保持同步。',
    docsHandbook: '中文手册',
    docsWiki: 'Wiki',
    platformsEyebrow: 'BUILD SURFACE',
    platformsTitle: '选择你的运行主线',
    platformsLede: 'Nullus 的平台状态按构建、运行和持续验证分别记录。选择平台前，先看清楚当前边界。',
    statusValidated: 'VALIDATED MAINLINE',
    statusBuildTarget: 'BUILD TARGET',
    statusLongTerm: 'LONG-TERM',
    platformWindowsText: 'MSVC / Visual Studio 2022，适合从 Editor 到桌面 Player 的完整开发路径。',
    platformLinuxText: 'GCC / Clang 构建入口，适合无界面构建、Vulkan 运行时和 CI 验证。',
    platformMacText: '提供原生构建目标与 Metal 后端，运行时验证属于独立的设备验收门槛。',
    platformFutureTitle: '长期方向',
    platformFutureText: '移动端、主机与 Web 目前不在构建和后端目标内，相关能力会随基础设施推进。',
    platformDetails: '平台详情',
    platformRoadmap: '查看路线图',
    platformNote: '平台矩阵区分“能构建”“能运行冒烟”和“有持续验证”，官网不会把目标平台写成已交付能力。',
    architectureEyebrow: 'UNDER THE HOOD',
    architectureTitle: '清晰的边界，持续的性能',
    architectureLede: 'Game Thread 产生命令，Render Thread 构建帧，RHI 负责有序提交。每一段都可观察，每一次扩展都有位置。',
    architectureLink: '阅读架构文档',
    workflowEyebrow: 'THE CREATION LOOP',
    workflowTitle: '从空项目到可玩的世界',
    workflowLede: '保持上下文，减少切换。你的场景、内容和逻辑沿着同一条主线成长。',
    stepOneTitle: '创建项目',
    stepOneText: '从 Launcher 创建或打开项目，直接进入 Editor。',
    stepTwoTitle: '组织场景',
    stepTwoText: '导入资产、创建 Prefab，用 Inspector 组合组件。',
    stepThreeTitle: '编写逻辑',
    stepThreeText: '用 C# 或 Lua 连接 GameObject、输入和时间系统。',
    stepFourTitle: '运行与打包',
    stepFourText: '在 Editor 内预览，使用 Build Profile 生成 Player。',
    galleryEyebrow: 'BUILT IN THE EDITOR',
    galleryTitle: '让每一帧都保持可见',
    galleryLink: '查看更多截图',
    startEyebrow: 'FIRST RUN',
    startTitle: '三条命令，进入你的第一个场景',
    startLede: '准备依赖、配置构建目录，然后启动 Editor。平台脚本保持清晰，项目入口保持一致。',
    terminalReady: 'Ready to build',
    ctaEyebrow: 'YOUR NEXT WORLD STARTS HERE',
    ctaTitle: '把引擎变成你的创作空间',
    ctaPrimary: '开始构建',
    ctaGithub: '访问 GitHub',
    footerTagline: '面向实时 3D 创作的 C++20 原生引擎。',
    footerExplore: '探索',
    footerResources: '资源',
    footerProject: '项目',
    footerStatus: 'Built for real-time creation',
  },
  en: {
    metaTitle: 'Nullus Engine | Native C++20 Engine for Real-Time 3D Creation',
    metaDescription: 'Nullus is a native C++20 engine for real-time 3D creation with an Editor, FrameGraph, DX12, Vulkan, Metal, C# and Lua scripting, asset workflows, and desktop Player builds.',
    navFeatures: 'Capabilities',
    navWorkflow: 'Workflow',
    navGallery: 'Showcase',
    navDocs: 'Docs',
    navPlatforms: 'Platforms',
    heroEyebrow: 'SOURCE AVAILABLE · REAL-TIME 3D',
    heroTitle: 'Build real-time 3D worlds on one native mainline',
    heroLede: 'Nullus is a native C++20 engine for real-time creation. Scenes, assets, scripts, the Editor, runtime, and multi-backend rendering stay in one coherent workflow.',
    heroPrimary: 'Start building',
    heroSecondary: 'Explore capabilities',
    scrollHint: 'Scroll to explore',
    proofReady: 'READY TO COMPILE',
    advantagesEyebrow: 'WHY NULLUS',
    advantagesTitle: 'Every layer is traceable. Every extension has a place.',
    advantagesLede: 'Nullus keeps authoring tools, runtime, and engine systems on one mainline. Start in the Editor or go straight into rendering, content, or scripting boundaries.',
    metricRuntime: 'ONE CONTENT PATH',
    metricThreads: 'RENDER CHANNELS',
    metricScripts: 'SCRIPT BACKENDS',
    metricCpp: 'C++ STANDARD',
    signalRuntimeTitle: 'One runtime from Editor to Player',
    signalRuntimeText: 'Edit scenes, assets, and scripts in the Editor, run them in Game, then ship them through a Build Profile. Content keeps one representation.',
    signalRhiTitle: 'Explicit RHI makes the performance path visible',
    signalRhiText: 'The Game Thread, Render Thread, and RHI Submit each own a clear stage. FrameGraph coordinates passes, resource states, and dependencies.',
    signalContentTitle: 'A source-to-asset path you can inspect',
    signalContentText: 'glTF, FBX, OBJ, PBR materials, Prefabs, and serialized scenes enter a project asset database with stable imported identities.',
    signalScriptTitle: 'C# and Lua share objects and lifecycle',
    signalScriptText: 'Both languages connect to the same GameObject, Component, input, and time systems. C# hot-reloads after an incremental build. Lua reloads on save.',
    featuresEyebrow: 'ENGINE SURFACE',
    featuresTitle: 'Designed around the work you actually do',
    featuresLede: 'From the first mesh to the final Player, every layer connects to a clear, observable, extensible engine mainline.',
    featureRenderTitle: 'Explicit multi-backend rendering',
    featureRenderText: 'FrameGraph, HLSL, and a unified RHI give DX12, Vulkan, and Metal one rendering language.',
    featureEditorTitle: 'Create inside the Editor',
    featureEditorText: 'Hierarchy, Scene View, Inspector, play controls, and Asset Browser form a daily editing loop.',
    featureAssetsTitle: 'Assets flow into the scene',
    featureAssetsText: 'Models, materials, textures, Prefabs, and serialized scenes connect to a project asset database.',
    featureScriptTitle: 'C# and Lua side by side',
    featureScriptText: 'Share a native scripting ABI, component lifecycle, input, and time systems while iterating in the Editor.',
    featureSimTitle: 'Make the world move',
    featureSimText: 'Physics, character control, animation, and particles share the same scene and runtime boundaries.',
    featureBuildTitle: 'From project to desktop Player',
    featureBuildText: 'Build Profiles collect dependencies, cook content, and assemble a runnable desktop Player.',
    learnMore: 'Learn more',
    docsEyebrow: 'DEVELOPER PATH',
    docsTitle: 'From the first command to the engine internals',
    docsLede: 'The site shows what Nullus can do. The handbook gets it running. Choose an entry point and continue into the real project files and workflows.',
    docsBuildTitle: 'Environment and build',
    docsBuildText: 'Prepare dependencies, configure CMake, and build the Editor, Launcher, or Player with the right platform entry point.',
    docsBuildMeta: 'Windows · Linux · macOS',
    docsEditorTitle: 'Use the Editor',
    docsEditorText: 'Learn Scene View, Game View, Hierarchy, Inspector, Asset Browser, and the shortcuts that shape daily work.',
    docsEditorMeta: 'Scene · Assets · Settings',
    docsArchitectureTitle: 'Understand the engine',
    docsArchitectureText: 'Follow modules, reflection, serialization, jobs, editor extensions, and plugin boundaries back into the source.',
    docsArchitectureMeta: 'Runtime · Editor · Modules',
    docsRead: 'Read the handbook',
    docsFoot: 'Docs/ is the handbook source. Chinese and English pages are kept in sync.',
    docsHandbook: 'Chinese handbook',
    docsWiki: 'Wiki',
    platformsEyebrow: 'BUILD SURFACE',
    platformsTitle: 'Choose your runtime mainline',
    platformsLede: 'Nullus records platform build, runtime, and validation status separately. Check the boundary before choosing a target.',
    statusValidated: 'VALIDATED MAINLINE',
    statusBuildTarget: 'BUILD TARGET',
    statusLongTerm: 'LONG-TERM',
    platformWindowsText: 'MSVC / Visual Studio 2022 for the full Editor-to-desktop-Player development path.',
    platformLinuxText: 'GCC / Clang build entry for headless builds, Vulkan runtime work, and CI validation.',
    platformMacText: 'A native build target and Metal backend are present. Runtime validation remains a separate device gate.',
    platformFutureTitle: 'Long-term direction',
    platformFutureText: 'Mobile, console, and Web targets are outside the current build and backend scope.',
    platformDetails: 'Platform details',
    platformRoadmap: 'View roadmap',
    platformNote: 'The matrix separates “can build”, “can smoke run”, and “continuously validated”. Target platforms are not presented as shipped capabilities.',
    architectureEyebrow: 'UNDER THE HOOD',
    architectureTitle: 'Clear boundaries. Sustained performance.',
    architectureLede: 'The Game Thread produces commands, the Render Thread builds frames, and the RHI submits in order. Every stage is observable and extensible.',
    architectureLink: 'Read the architecture docs',
    workflowEyebrow: 'THE CREATION LOOP',
    workflowTitle: 'From empty project to playable world',
    workflowLede: 'Keep context and reduce switching. Your scenes, content, and logic grow along the same mainline.',
    stepOneTitle: 'Create a project',
    stepOneText: 'Create or open a project from the Launcher and enter the Editor.',
    stepTwoTitle: 'Shape the scene',
    stepTwoText: 'Import assets, create Prefabs, and compose components in the Inspector.',
    stepThreeTitle: 'Write gameplay',
    stepThreeText: 'Connect GameObjects, input, and time with C# or Lua.',
    stepFourTitle: 'Run and package',
    stepFourText: 'Preview in the Editor and build a Player with a Build Profile.',
    galleryEyebrow: 'BUILT IN THE EDITOR',
    galleryTitle: 'Keep every frame in view',
    galleryLink: 'View more screenshots',
    startEyebrow: 'FIRST RUN',
    startTitle: 'Three commands to your first scene',
    startLede: 'Prepare dependencies, configure a build directory, then launch the Editor. Platform scripts stay explicit and the project entry stays consistent.',
    terminalReady: 'Ready to build',
    ctaEyebrow: 'YOUR NEXT WORLD STARTS HERE',
    ctaTitle: 'Turn the engine into your creative space',
    ctaPrimary: 'Start building',
    ctaGithub: 'Open GitHub',
    footerTagline: 'A native C++20 engine for real-time 3D creation.',
    footerExplore: 'Explore',
    footerResources: 'Resources',
    footerProject: 'Project',
    footerStatus: 'Built for real-time creation',
  },
};

const platformCode = {
  windows: {
    backend: 'DX12 default',
    code: `<span class="terminal-comment"># clone</span>\ngit clone https://github.com/NullusEngine/Nullus.git\ncd Nullus\n\n<span class="terminal-comment"># prepare + build Editor</span>\n.<span class="terminal-prompt">\\</span>SetupDependencies.bat\ncmake -S . -B build -G <span class="terminal-string">"Visual Studio 17 2022"</span> -A x64\ncmake --build build --config Debug --target Editor`,
  },
  linux: {
    backend: 'Vulkan default',
    code: `<span class="terminal-comment"># clone</span>\ngit clone https://github.com/NullusEngine/Nullus.git\ncd Nullus\n\n<span class="terminal-comment"># prepare + build Editor</span>\n./SetupDependencies.sh\n./build_linux.sh debug`,
  },
  macos: {
    backend: 'Metal default',
    code: `<span class="terminal-comment"># clone</span>\ngit clone https://github.com/NullusEngine/Nullus.git\ncd Nullus\n\n<span class="terminal-comment"># prepare + build Editor</span>\n./SetupDependencies.sh\n./build_macos.sh debug`,
  },
};

const setTextKeepingChildren = (element, value) => {
  const textNode = Array.from(element.childNodes).find((node) => node.nodeType === Node.TEXT_NODE);
  if (textNode) {
    textNode.nodeValue = `${value} `;
  } else {
    element.textContent = value;
  }
};

const applyLanguage = (language) => {
  const dictionary = translations[language];
  document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
  document.title = dictionary.metaTitle;
  document.querySelector('meta[name="description"]')?.setAttribute('content', dictionary.metaDescription);
  document.querySelector('meta[property="og:title"]')?.setAttribute('content', dictionary.metaTitle);
  document.querySelector('meta[property="og:description"]')?.setAttribute('content', dictionary.metaDescription);
  document.querySelector('meta[name="twitter:title"]')?.setAttribute('content', dictionary.metaTitle);
  document.querySelector('meta[name="twitter:description"]')?.setAttribute('content', dictionary.metaDescription);
  document.querySelectorAll('[data-i18n]').forEach((element) => {
    const value = dictionary[element.dataset.i18n];
    if (value) setTextKeepingChildren(element, value);
  });

  document.querySelectorAll('[data-doc-link]').forEach((element) => {
    const destination = language === 'zh' ? element.dataset.docZh : element.dataset.docEn;
    if (destination) element.href = destination;
  });

  const languageToggle = document.querySelector('[data-language-toggle]');
  if (languageToggle) {
    languageToggle.textContent = language === 'zh' ? 'EN' : '中';
    languageToggle.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : '切换为中文');
  }

  localStorage.setItem('nullus-language', language);
};

const setupLanguageToggle = () => {
  const languageToggle = document.querySelector('[data-language-toggle]');
  if (!languageToggle) return;

  const pathLanguage = window.location.pathname.toLowerCase().startsWith('/en/')
    ? 'en'
    : window.location.pathname.toLowerCase().startsWith('/zh-cn/')
      ? 'zh'
      : null;
  const savedLanguage = localStorage.getItem('nullus-language');
  const initialLanguage = pathLanguage ?? (savedLanguage === 'en' ? 'en' : 'zh');
  applyLanguage(initialLanguage);

  languageToggle.addEventListener('click', () => {
    const nextLanguage = document.documentElement.lang === 'zh-CN' ? 'en' : 'zh';
    if (pathLanguage) {
      const nextPath = nextLanguage === 'en' ? '/en/' : '/zh-cn/';
      window.location.assign(`${nextPath}${window.location.hash}`);
      return;
    }
    applyLanguage(nextLanguage);
  });
};

const setupNavigation = () => {
  const header = document.querySelector('[data-header]');
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');

  const updateHeader = () => {
    header?.classList.toggle('is-scrolled', window.scrollY > 12);
  };

  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  menuToggle?.addEventListener('click', () => {
    const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!isOpen));
    menuToggle.setAttribute('aria-label', isOpen ? '打开菜单' : '关闭菜单');
    mobileMenu?.classList.toggle('is-open', !isOpen);
  });

  mobileMenu?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menuToggle?.setAttribute('aria-expanded', 'false');
      menuToggle?.setAttribute('aria-label', '打开菜单');
      mobileMenu.classList.remove('is-open');
    });
  });
};

const setupReveal = () => {
  const revealElements = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealElements.forEach((element) => element.classList.add('is-visible'));
    return;
  }

  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      currentObserver.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -35px' });

  revealElements.forEach((element) => observer.observe(element));
};

const setupPlatformTabs = () => {
  const code = document.querySelector('#terminal-code code');
  const backend = document.querySelector('[data-terminal-backend]');
  const tabs = document.querySelectorAll('[data-platform]');
  if (!code || !backend || !tabs.length) return;

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      const platform = tab.dataset.platform;
      const selected = platformCode[platform];
      if (!selected) return;
      tabs.forEach((item) => {
        const isActive = item === tab;
        item.classList.toggle('is-active', isActive);
        item.setAttribute('aria-selected', String(isActive));
      });
      code.innerHTML = selected.code;
      backend.textContent = selected.backend;
    });
  });
};

const setupCopyButton = () => {
  const copyButton = document.querySelector('[data-copy-target]');
  const label = copyButton?.querySelector('[data-copy-label]');
  const target = document.querySelector(`#${copyButton?.dataset.copyTarget}`);
  if (!copyButton || !label || !target) return;

  copyButton.addEventListener('click', async () => {
    const original = document.documentElement.lang === 'zh-CN' ? '复制命令' : 'Copy commands';
    const copied = document.documentElement.lang === 'zh-CN' ? '已复制' : 'Copied';
    try {
      await navigator.clipboard.writeText(target.textContent.trim());
      label.textContent = copied;
    } catch {
      label.textContent = document.documentElement.lang === 'zh-CN' ? '请手动复制' : 'Copy manually';
    }
    window.setTimeout(() => { label.textContent = original; }, 1800);
  });
};

const setupYear = () => {
  const year = document.querySelector('[data-current-year]');
  if (year) year.textContent = new Date().getFullYear();
};

const setupHashNavigation = () => {
  const header = document.querySelector('[data-header]');
  if (!header) return;
  const syncHashTarget = () => {
    if (!window.location.hash) return;
    const target = document.querySelector(window.location.hash);
    if (!target) return;
    window.setTimeout(() => {
      const offset = header.getBoundingClientRect().height + 18;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
    }, 0);
  };
  window.addEventListener('hashchange', syncHashTarget);
  syncHashTarget();
};

setupLanguageToggle();
setupNavigation();
setupReveal();
setupPlatformTabs();
setupCopyButton();
setupYear();
setupHashNavigation();
