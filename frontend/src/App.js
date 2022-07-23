import React from "react";

export default function App() {
    URL_API = "http://85.195.220.234:42334/api/version";

    const [backEndVersion, setBackEndVersion] = React.useState("0");

    console.log(backEndVersion);

    // React.useEffect(() => {
    //     // Define inner function
    //     async function getVersion() {
    //         const response = await fetch(URL_API)
    //         console.log(response)
    //         const response_json = await response.json()
    //         setBackEndVersion(response_json.data.version)
    //         console.log("update")
    //     }
    //     // Run inner function
    //     getVersion()
    //     return () => {
    //         // Destructor
    //     }
    // }, [])

    React.useEffect(() => {
        console.log(URL_API);
        const version = fetch(URL_API)
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                return data.data.version;
            })
            .catch((err) => {
                throw new Error(err);
            });
        setBackEndVersion(version);
        return () => {};
    }, []);

    return <div className="container">Backend version: {backEndVersion}</div>;
}
