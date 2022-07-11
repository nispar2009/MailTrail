compose = fr => {
    const from = "<input type='hidden' value='" + fr + "' name='from'>"
    const to = "<input type='email' class='form form-line' placeholder='To...' name='to'><br><br>"
    const sub = "<input type='text' class='form form-line' placeholder='Subject...' name='sub'><br><br>"
    const cnt = "<textarea class='form form-line' placeholder='Body...' name='cnt'></textarea><br><br>"
    const send = "<button class='btn btn-blue-outline' type='submit'>Send</button>"
    return "<form method='POST' action='/send-mail' target='_blank'>" + to + from + sub + cnt + send + "</form>"
}

guest = () => {
    const from = "<input type='hidden' value='' name='from'>"
    const to = "<input type='email' class='form form-line' placeholder='To...' name='to'><br><br>"
    const sub = "<input type='text' class='form form-line' placeholder='Subject...' name='sub'><br><br>"
    const cnt = "<textarea class='form form-line' placeholder='Body...' name='cnt'></textarea><br><br>"
    const send = "<button class='btn btn-blue-outline' type='submit'>Send</button>"
    return "<h2 class='text-green'>Continue as a guest</h2><form method='POST' action='/send-mail'>" + from + to + sub + cnt + send + "</form>"
}