chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {

    if (msg.cmd !== "scan") return;

    fetch("http://127.0.0.1:5050/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: msg.url,
            text: ""
        })
    })
    .then(r => r.json())
    .then(j => sendResponse({ ok: true, data: j }))
    .catch(() => sendResponse({ ok: false }));

    return true;
});
