import Navbar from './Navbar.tsx'
import { Center, Box, Text } from '@chakra-ui/react'
import AdminTable from './adminTable.tsx'
export default function Users() {
   return (
      <div>
         <Navbar />
         <Box mt="4rem">
            <Center>
               <Text mt={'8'}>User List Page</Text>
            </Center>
         </Box>
         <Box m={4}>
            <AdminTable />
         </Box>
      </div>
   )
}
