function doGet() {
  
  const threads = GmailApp.getInboxThreads()
  
  for (x in threads) {

    let subject = threads[x].getFirstMessageSubject()
    
    if (subject.includes('No-IP Verification Code:')) {

      let code = subject.split(': ')[1]
      
      return ContentService.createTextOutput(code)
      
    }
    
  }
  
}