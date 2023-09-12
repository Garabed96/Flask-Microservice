import Navbar from './Navbar.tsx'
import { Center, Box, Text } from '@chakra-ui/react'

export default function JournalEntry() {
   return (
      <div>
         <Navbar />
         <Box mt="4rem">
            <Center>
               <Text>Journal Entry Page</Text>
            </Center>
         </Box>
      </div>
   )
}
