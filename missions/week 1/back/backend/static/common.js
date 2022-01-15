.t-relative {
  position: relative;
}

.t--z-50 {
  z-index: -50;
}

.t-my-\[0px\] {
  margin-top: 0px;
  margin-bottom: 0px;
}

.t-mt-3 {
  margin-top: 0.75rem;
}

.t-mt-2 {
  margin-top: 0.5rem;
}

.t-mt-12 {
  margin-top: 3rem;
}

.t-block {
  display: block;
}

.t-flex {
  display: flex;
}

.t-grid {
  display: grid;
}

.t-min-h-screen {
  min-height: 100vh;
}

.t-w-full {
  width: 100%;
}

.t-max-w-screen-md {
  max-width: 768px;
}

.t-flex-1 {
  flex: 1 1 0%;
}

.t-grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

.t-flex-col {
  flex-direction: column;
}

.t-items-center {
  align-items: center;
}

.t-justify-center {
  justify-content: center;
}

.t-gap-\[20px\] {
  gap: 20px;
}

.t-overflow-hidden {
  overflow: hidden;
}

.t-whitespace-nowrap {
  white-space: nowrap;
}

.t-rounded {
  border-radius: 0.25rem;
}

.t-object-cover {
  -o-object-fit: cover;
     object-fit: cover;
}

.t-py-\[20px\] {
  padding-top: 20px;
  padding-bottom: 20px;
}

.t-pt-\[56px\] {
  padding-top: 56px;
}

.t-text-center {
  text-align: center;
}

.t-text-\[20px\] {
  font-size: 20px;
}

.t-font-bold {
  font-weight: 700;
}

.t-italic {
  font-style: italic;
}

.t-text-black {
  --tw-text-opacity: 1;
  color: rgb(0 0 0 / var(--tw-text-opacity));
}

.t-text-gray-400 {
  --tw-text-opacity: 1;
  color: rgb(156 163 175 / var(--tw-text-opacity));
}

.t-no-underline {
  -webkit-text-decoration-line: none;
          text-decoration-line: none;
}

.t-transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

@font-face {
  font-family: 'GmarketSansMedium';

  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');

  font-weight: normal;

  font-style: normal;
}

html > body ul,
html > body li {
  margin:0;
  padding:0;
  list-style:none;
}

html > body {
  font-family: "GmarketSansMedium";
  text-underline-position: under;
}

html > body :is(h1, h2, h3, h4, h5, h6) {
  font-weight:normal;
  margin:0;
  font-size:1rem;
}

.before\:t-absolute::before {
  content: var(--tw-content);
  position: absolute;
}

.before\:t-inset-0::before {
  content: var(--tw-content);
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
}

.before\:t-bg-\[\#00000000\]::before {
  content: var(--tw-content);
  background-color: #00000000;
}

.before\:t-transition-all::before {
  content: var(--tw-content);
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.before\:t-content-\[\'\'\]::before {
  --tw-content: '';
  content: var(--tw-content);
}

.after\:t-absolute::after {
  content: var(--tw-content);
  position: absolute;
}

.after\:t-top-\[50\%\]::after {
  content: var(--tw-content);
  top: 50%;
}

.after\:t-left-\[50\%\]::after {
  content: var(--tw-content);
  left: 50%;
}

.after\:t-hidden::after {
  content: var(--tw-content);
  display: none;
}

.after\:t-translate-y-\[-50\%\]::after {
  content: var(--tw-content);
  --tw-translate-y: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.after\:t-translate-x-\[-50\%\]::after {
  content: var(--tw-content);
  --tw-translate-x: -50%;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.after\:t-whitespace-nowrap::after {
  content: var(--tw-content);
  white-space: nowrap;
}

.after\:t-rounded::after {
  content: var(--tw-content);
  border-radius: 0.25rem;
}

.after\:t-border-2::after {
  content: var(--tw-content);
  border-width: 2px;
}

.after\:t-border-solid::after {
  content: var(--tw-content);
  border-style: solid;
}

.after\:t-border-white::after {
  content: var(--tw-content);
  --tw-border-opacity: 1;
  border-color: rgb(255 255 255 / var(--tw-border-opacity));
}

.after\:t-p-2::after {
  content: var(--tw-content);
  padding: 0.5rem;
}

.after\:t-text-white::after {
  content: var(--tw-content);
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity));
}

.after\:t-no-underline::after {
  content: var(--tw-content);
  -webkit-text-decoration-line: none;
          text-decoration-line: none;
}

.after\:t-transition-all::after {
  content: var(--tw-content);
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.after\:t-content-\[attr\(data-before\)\]::after {
  --tw-content: attr(data-before);
  content: var(--tw-content);
}

.hover\:t-bg-red-500:hover {
  --tw-bg-opacity: 1;
  background-color: rgb(239 68 68 / var(--tw-bg-opacity));
}

.t-group:hover .group-hover\:t-scale-110 {
  --tw-scale-x: 1.1;
  --tw-scale-y: 1.1;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.t-group:hover .group-hover\:t-bg-red-500 {
  --tw-bg-opacity: 1;
  background-color: rgb(239 68 68 / var(--tw-bg-opacity));
}

.t-group:hover .group-hover\:t-text-blue-500 {
  --tw-text-opacity: 1;
  color: rgb(59 130 246 / var(--tw-text-opacity));
}

.t-group:hover .group-hover\:t-underline {
  -webkit-text-decoration-line: underline;
          text-decoration-line: underline;
}

.t-group:hover .group-hover\:before\:t-bg-\[\#00000055\]::before {
  content: var(--tw-content);
  background-color: #00000055;
}

.t-group:hover .group-hover\:after\:t-block::after {
  content: var(--tw-content);
  display: block;
}

@media (min-width: 640px) {
  .sm\:t-grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 768px) {
  .md\:t-grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  @media (min-width: 640px) {
    .lg\:sm\:t-grid-cols-4 {
      grid-template-columns: repeat(4, minmax(0, 1fr));
    }
  }
}