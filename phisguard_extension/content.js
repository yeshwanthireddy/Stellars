console.log("PhishGuard active");

// Catch shortened URLs before redirect
function isShortener(url) {
    return (
        url.includes("bit.ly") ||
        url.includes("tinyurl") ||
        url.includes("t.co") ||
        url.includes("goo.gl")
    );
}

document.addEventListener("click", function (e) {

    const a = e.target.closest("a");
    if (!a) return;

    const url = a.href;
    if (!url) return;

    // Always intercept short links
    if (isShortener(url)) {
        e.preventDefault();
        e.stopImmediatePropagation();
        scan(url);
        return;
    }

    // Intercept normal links
    e.preventDefault();
    e.stopImmediatePropagation();
    scan(url);

}, true);


function scan(url) {

    chrome.runtime.sendMessage(
        {
            cmd: "scan",
            url: url
        },
        res => {

            if (!res || !res.ok) {
                alert("PhishGuard backend offline");
                return;
            }

            const d = res.data;

            alert(
                "PhishGuard Scan Result\n\n" +
                "Decision: " + d.decision +
                "\nRisk: " + d.score
            );

            if (d.decision === "SAFE") {
                window.location.href = url;
                return;
            }

            if (confirm("⚠️ Suspicious link. Open anyway?")) {
                window.location.href = url;
            }
        }
    );
}
