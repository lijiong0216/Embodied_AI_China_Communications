$ErrorActionPreference = 'Stop'
$paperSource = Split-Path -Parent $PSScriptRoot
$paperBuild = Join-Path $paperSource 'tmp/pdfs/submission/build'
$paperOutput = Join-Path $paperSource 'output/pdf'
$paperPython = 'C:/Users/23880/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
New-Item -ItemType Directory -Path $paperBuild -Force | Out-Null
New-Item -ItemType Directory -Path $paperOutput -Force | Out-Null
Push-Location $paperBuild
try {
    for ($paperPass = 1; $paperPass -le 3; $paperPass++) {
        & pdflatex -interaction=nonstopmode -halt-on-error "--include-directory=$paperSource" (Join-Path $PSScriptRoot 'China_Communications_Main_Document.tex') | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "Main Document LaTeX build failed on pass $paperPass." }
    }
    Copy-Item -LiteralPath (Join-Path $paperBuild 'China_Communications_Main_Document.pdf') -Destination $paperOutput
    & $paperPython (Join-Path $PSScriptRoot 'create_title_page.py')
    if ($LASTEXITCODE -ne 0) { throw 'Title Page build failed.' }
    & pdftoppm -r 115 -png (Join-Path $paperOutput 'China_Communications_Main_Document.pdf') (Join-Path $paperBuild 'main') | Out-Null
    & pdftoppm -r 140 -png (Join-Path $paperOutput 'China_Communications_Title_Page.pdf') (Join-Path $paperBuild 'title') | Out-Null
    & pdfinfo (Join-Path $paperOutput 'China_Communications_Main_Document.pdf')
    & pdfinfo (Join-Path $paperOutput 'China_Communications_Title_Page.pdf')
} finally {
    Pop-Location
}
