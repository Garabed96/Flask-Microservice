import { FormControl, FormLabel, Input, FormHelperText } from '@chakra-ui/react'

export default function AccountEditForm() {
   return (
      <FormControl>
         <FormLabel>Email address</FormLabel>
         <Input type="email" />
         <FormHelperText>We'll never share your email.</FormHelperText>
      </FormControl>
   )
}
